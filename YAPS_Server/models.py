from django.db import models
import datetime

# Create your models here.
class Place(models.Model):
    TYPES = (
       ('O', 'Office'),
       ('A', 'Airport')
    )

    p_id = models.BigAutoField(primary_key=True)
    pName = models.CharField(max_length=200, default='Nil')
    type = models.CharField(max_length=1, choices=TYPES, default='O')
    inactives = models.IntegerField(default=0)
    actives = models.IntegerField(default=0)
    latitude = models.FloatField(default=0)
    longtitude = models.FloatField(default=0)

    def __str__(self):
        return self.pName + ": " + str(self.p_id)

class Group(models.Model):
    TYPES = (
       ('OA', 'Office to Airport'),
       ('AO', 'Airport to Office'),
       ('OO', 'Office to Office')
    )

    STATES = (
       ('W', 'Waiting'),
       ('A', 'Assigned'),
       ('D', 'Departed')
    )

    STYPES = (
       ('E', 'Exclusive'),
       ('W', 'Willing'),
       ('N', 'Non Willing')
    )

    g_id = models.BigAutoField(primary_key=True)
    numPassenger = models.IntegerField(default=0)
    share = models.CharField(max_length=1, choices=STYPES, default='W')
    travelType = models.CharField(max_length=2, choices=TYPES, default='OA')
    pickupTime = models.DateTimeField(blank=True, null=True,default=datetime.datetime.today)
    state = models.CharField(max_length=1, choices=STATES, default='W')
    startLocation = models.ForeignKey(Place, on_delete=models.DO_NOTHING, related_name="startLoc")
    endLocation = models.ForeignKey(Place, on_delete=models.DO_NOTHING, related_name="endLoc")

    def __str__(self):
        return str([self.g_id, self.numPassenger, self.share,self.pickupTime, self.startLocation, self.endLocation])

class Passenger(models.Model):
    p_id = models.BigAutoField(primary_key=True)
    pName = models.CharField(max_length=200, default='Nil')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.pName + ": " + str(self.p_id)

class Driver(models.Model):
    d_id = models.BigAutoField(primary_key=True)
    dName = models.CharField(max_length=200, default='Nil')
    phone = models.CharField(max_length=20, default='Nil')

    def __str__(self):
        return self.dName + ": " + str(self.d_id)

class Car(models.Model):
    STATES = (
       ('INA', 'Inactive'),
       ('RAO', 'Rest at Office'),
       ('LFO', 'Left from Office'),
       ('RAA', 'Rest at Airport'),
       ('LFA', 'Left from Airport'),
    )

    c_id = models.BigAutoField(primary_key=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    seats = models.IntegerField(default=4)
    state = models.CharField(max_length=3, choices=STATES, default='INA')
    location = models.ForeignKey(Place, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return str([self.c_id, self.driver, self.seats, self.state, self.location])

class Booking(models.Model):
    b_id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING)
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    people = models.IntegerField(default=0)

    def __str__(self):
        return str(self.b_id)