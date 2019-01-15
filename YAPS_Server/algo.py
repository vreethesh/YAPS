def knapSack(W, wt, val, n): 
    K = [[0 for w in range(W + 1)] 
            for i in range(n + 1)] 

    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1]  
                  + K[i - 1][w - wt[i - 1]], 
                               K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 

    # stores the result of Knapsack 
    res = K[n][W] 
    #print(res) 
    out=[]
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break 
        if res == K[i - 1][w]: 
            continue
        else:
            out.append((i-1,wt[i - 1]))
            res = res - val[i - 1] 
            w = w - wt[i - 1]
    return res, out
  

def assignPool(groups, cars):
   print(cars)
   for start in [8,9,10,11,12]:
      for end in [8,9,10,11,12]:
         if start == end:
            continue
         e=[]
         n=[]
         w=[]
         for group in groups:
             #iprint(group)
             if group["startLocation_id"]==start and group["endLocation_id"]==end:
               #print(group)
               if group['share'] == 'E':
                  e.append((group['g_id'], group['numPassenger'], group["pickupTime"]))
               elif group['share'] == 'N':
                  n.append((group['g_id'], group['numPassenger'], group["pickupTime"]))
               elif group['share'] == 'W':
                  w.append((group['g_id'], group['numPassenger'], group["pickupTime"]))
               else:
                  print("ERROR: " + str(group))
            

         c=[]
         for car in cars:
            #print(car)
            if car['state'] in ['RAO', 'RAA']:
               c.append((car['c_id'], car['driver_id'], car["seats"]))
            else:
               print("ERROR: " + car)
         input()
         e=sorted(e, key=lambda e: e[1])
         n=sorted(n, key=lambda n: n[1])
         w=sorted(w, key=lambda w: w[1])
         c=sorted(c, key=lambda c: c[-1])
         
         print("E",e)
         print("N",n)
         print("W",w)
         print("C",c)
         ex_output = []
         for each in e:
            for i in range(len(c)):
               if each[1] > c[i][-1]:
                  continue
               elif each[1] <= c[i][-1]:
                  ex_output.append((each[0], c[i][0]))
                  del c[i]
                  break
               print("ERROR: ", each[1], c[i][-1])
         
         no_output=[]
         passengers=[1]*len(n)
         value = []
         for each in n:
            value.append(each[1])
            for i in range(len(c)):
               W = c[i][-1]
               num = len(value)
               res, out = knapSack(W,  value,passengers, num)
               #out = [o[0] for o in out]
               print(out)
               if out != []:
                  pass1=False
                  print(len(out), c[i])
                  if len(out) == c[i][-1]:
                     if pass1:
                        break
                     for each1 in out:
                        no_output.append((each[0], c[i][0]))
                        del c[i]
                        pass1 = True
                        break
                  if len(out) < c[i][-1]:
                     for each1 in out:
                        no_output.append((each[0], c[i][0]))
                        c[i] = (c[i][0],c[i][1],c[i][-1]-each[1])
               #print("ERROR: ", each[1], c[i][-1])

         c=sorted(c, key=lambda c: c[-1])
         
         wi_output=[]
         passengers=[]
         value = [1]*len(n)
         for each in n:
            passengers.append(each[1])
         for i in range(len(c)):
            W = c[i][-1]
            num = len(value)
            res, out = knapSack(W, passengers, value, num)
            if out != []:
               if len(out) == c[i][-1]:
                  for each in out:
                     wi_output.append((each[0], c[i][0]))
                     del c[i]
                     break
               if len(out) < c[i][-1]:
                  for each in out:
                     wi_output.append((each[0], c[i][0]))
                     c[i] = (c[i][0],c[i][1],c[i][-1]-each[1])               
                     break
               # Driver code 
               # val = [ 60, 100, 120 ] 
               # wt = [ 10, 20, 30 ] 
               # W = 50
               # n = len(val) 
                     
               # printknapSack(W, wt, val, n)
         yield ex_output, no_output, wi_output