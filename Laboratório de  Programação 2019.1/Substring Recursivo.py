x = "Paralalepipedo"
pt1 = 0
pt2 = 1

def substringREC(s,n,p1,p2):
    if  x.index(x[pt2-1]) == x.index(x[-1]):
        print(x[pt1:pt2])
        y = x[:pt2]
        pt1 += 1
        pt2 = pt1+1

    else:

        print(x[pt1:pt2])
        z= x[pt1:pt2]
        pt2 += 1

substringREC(x,14,pt2,pt1)