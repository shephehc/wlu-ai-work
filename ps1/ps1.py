import numpy as np

def readData(d):
    data = np.loadtxt(fname = d, dtype=str)
    x1  = np.empty(0)
    x2 = np.empty(0)
    y = np.empty(0)
    z = np.empty(0)

    for i in range(1, len(data)):
        #print(data[i,0])
        x1 = np.append(x1, data[i,0]).astype(float)
        x2 = np.append(x2, data[i,1]).astype(float)
        y = np.append(y, data[i,2]).astype(float)
        z = np.append(z, data[i,3]).astype(float)
    
    print("Part 1: Individual Least Squares for x1 and x2")
    m1 = np.sum((x1-np.mean(x1)*(np.sum(y-np.mean(y))))/ np.sum(np.square((x1-np.mean(x1)))))
    b1 = np.mean(y) - m1*np.mean(x1)
    print("y = " + str(round(m1, 2)) + "x1 " + str(round(b1, 2)))


    #y=mx2+b

    m2 = np.sum((x2-np.mean(x2)*(np.sum(y-np.mean(y))))/ np.sum(np.square((x2-np.mean(x2)))))
    b2 = np.mean(y) - m2*np.mean(x2)
    print("y = " + str(round(m2, 2)) + "x2 " + str(round(b2, 2)))
    
    print("\nPart 2:\n")
    a = np.vstack([(x1, x2), np.ones(len(x1))]).T
    w1, w2, b = np.linalg.lstsq(a, y, rcond=None)[0]
    print("y = " + str(round(w1, 2)) + "x1 + " + str(round(w2,2)) + "x2 " + str(round(b, 2)))

    #Part 3

    
    print("\nPart 3:\n")
    abv = 0 #above 0 class
    blw = 0 #below 0 class
    for i in range(1,len(data)-1):
        #print(x1[i]*w1 + x2[i]*w2 + b)
        if x1[i]*w1 + x2[i]*w2 + b >0:
            #print('abv')
            abv +=1
        else:
            blw +=1
            #print('blw')
    abvpct = abv / len(data)
    blwpct = 1-abvpct
    print(round(abvpct,2), "% Above")
    print(round(blwpct,2 ), "% Below")

    ones = 0
    zeros = 0
    '''for i in range(len(z)):
        if z[i] == 0:
            zeros+=1
        else:
            ones+=1'''
    #print(z)
    #print(ones, zeros)
    
    for j in range(25):
        if z[j] == 0:
            zeros+=1
        else:
            ones+=1
    print(ones, zeros)
    zeros=ones=0
    for j in range(50):
        if z[j] == 0:
            zeros+=1
        else:
            ones+=1
    print(ones, zeros)
    zeros=ones=0
    for j in range(75):
        if z[j] == 0:
            zeros+=1
        else:
            ones+=1
    print(ones, zeros)
    zeros=ones=0
        
    

fname = 'assign1_data.txt'

readData(fname)

