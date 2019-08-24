S = "BACBAD"
T = "ABAZDC"
SCL = Matriz n x m
for i in range(n):
    for j in range(m):
        if s[i]!=T[j]:
            SCL[i,j] = max(SCL[i-1,j],SCL[i,j-1])
        else:
            SCL[i,j] = SCL[i-1,j-1]+1


def max(x,y):
    if x>y:
        return x
    return y