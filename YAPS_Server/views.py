from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .algo import *
from django.db.models import Q

flag = 0
msg = ""

# Create your views here.
def index(request):
    global flag, msg
    template_name = r'YAPS/index.html'
    pls = list(Place.objects.values())
    context = {
        "flag": flag,
        "msg": msg,
        "places": pls
    }

    flag = 0
    msg = ""

    return render(request, template_name, context)

def search(request):
    if request.method == "GET":
        res = "Results"
        query = request.GET.get('q', 'query')
        if query != "query":
            r = Group.objects.filter(state='W').values()
            c = Car.objects.filter(Q(state = 'RAO') | Q(state = 'RAA')).values()
            for ex_output, no_output, wi_output in  assignPool(r,c):
                print(ex_output, no_output, wi_output),
            #print(list(r))
        return HttpResponse(res)

def passReg(request):
    global flag, msg
    if request.method == "POST":
        nPas = int(request.POST.get('nPas'))
        share = request.POST.get('share')
        pLoc = request.POST.get('pickup')
        dest = request.POST.get('dest')
        pTime = request.POST.get('pTime')

        from datetime import datetime
        temp_date = datetime.strptime(pTime, "%Y-%m-%dT%H:%M").strftime( '%Y-%m-%d %H:%M:%S')
        print("Time", temp_date)
        temp_date = datetime(int(pTime[:4]), int(pTime[5:7]), int(pTime[8:10]), int(pTime[11:13]),int(pTime[14:]))
        pTime = temp_date

        #pTime = pTime.strftime('%Y-%m-%dT%H:%M:%S', datetime())
        guests = []
        for i in range(nPas):
            g = request.POST.get('guest_' + str(i))
            if g is not None or g != "":
                guests.append(Passenger(pName=g))
            else:
                nPas -= 1

        pLoc = Place.objects.get(p_id=pLoc)
        dest = Place.objects.get(p_id=dest)

        tType = ''
        if pLoc.type == 'A':
            tType = 'OA'
        else:
            if dest.type == 'A':
                tType = 'AO'
            else:
                tType = 'OO'
        
        g = Group(numPassenger=nPas, share=share, travelType=tType, pickupTime=pTime, state='W', startLocation=pLoc, endLocation=dest)
        g.save()

        for passn in guests:
            passn.group = g
            passn.save()

        flag = 1
        msg = "Passenger registered successfully"

    return redirect('index')
        
def carReg(request):
    global flag, msg
    if request.method == "POST":
        cnum = request.POST.get('cno')
        dname = request.POST.get('usr')
        num = request.POST.get('phn')
        seats = request.POST.get('seats')

        d = Driver(dName=dname, phone=num)
        d.save()
        c = Car(driver=d, seats=int(seats))
        c.save()

        flag = 1
        msg = "Car registered successfully"

    return redirect('index')