N, M = map(int, input().split())
dicionário = [0 for x in range(N)]
for i in range(N):
    dicionário[i]= input()
palavrasusuario = [0 for x in range(M)]
for j in range(M):
    palavrasusuario[j] = input()

def minimo(x,y,z):
    resul = 0
    if x < y:
        resul = x
    else:
        resul = y
    if z < resul:
        resul= z
    return resul

def distEdit(a,b,A,B):
    M = [[0 for x in range(b)] for x in range(a)]
    for i in range(a):
        M[i][0] = i
    for j in range(b):
        M[0][j] = j
    for k in range(1,a):
        for l in range(1,b):
            if A[k-1] == B[l-1]:
                C = 0
            else:
                C = 1
            M[k][l] = minimo(M[(k-1)][l]+1,M[k][l-1]+1,M[k-1][l-1]+C)
    return (M[k][l])

for x in range(len(palavrasusuario)):
    P = ''
    for y in range(len(dicionário)):
        if len(palavrasusuario[x]) - len(dicionário[y])>2:
            pass
        elif distEdit(len(palavrasusuario[x])+1,len(dicionário[y])+1,palavrasusuario[x],dicionário[y]) <= 2:
            P += (dicionário[y] + ' ')
    if P != '':
        if x == len(palavrasusuario)-1:
            print(P,end='')
        else:
            print(P)
    else:
        print(' ')

