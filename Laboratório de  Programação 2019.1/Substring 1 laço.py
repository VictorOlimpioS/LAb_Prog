x = "paralelepipedo"
pt1 = 0
pt2 = 0
T = len(x)

while pt1 <= T:
    if pt2 == T:
        print(x[pt1:pt2])
        y = x[:pt2]
        pt1 += 1
        pt2 = pt1

    else:
        print(x[pt1:pt2])
        h = x[pt1:pt2]
        pt2 += 1









