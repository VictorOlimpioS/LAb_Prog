L, C = map(int, input().split()) #recebendo o tamanho da Matris dos robôs (Linha e coluna) e o número de interações
M = []
for i in range(L): #Montando a Matriz
    matriz = input()
    matriz = list(matriz)
    M.append(matriz)
numjogadas  = int(input())
jogadas = []
for j in range(numjogadas): #Montando a Matriz
    matriz2 = input().split()
    matriz2 = tuple(map(int,matriz2))
    jogadas.append(matriz2)
def mapnavio(a,b,L,C):
    M[a][b] = 'N'
    coordenadas = [(a,b)]
    navio = []
    T = 0
    while coordenadas:
        a,b = coordenadas.pop(0)
        navio.append((a+1,b+1))
        if navio[-1] in jogadas:
                T += 1
        if a+1<=L:
            if M[a+1][b] == "#":
                tupla = (a+1,b)
                coordenadas.append(tupla)
                M[a+1][b] = "N"
        if a-1>=0:
            if M[a-1][b] == "#":
                tupla = (a-1,b)
                coordenadas.append(tupla)
                M[a-1][b] = "N"
        if b+1<=C:
            if M[a][b+1] == "#":
                tupla = (a,b+1)
                coordenadas.append(tupla)
                M[a][b+1] = "N"
        if b-1>=0:
            if M[a][b-1] == "#":
                tupla = (a,b-1)
                coordenadas.append(tupla)
                M[a][b-1] = "N"
    if len(navio) == T:
        return 1
    else:
        return 0

jogo = 0
for k in range(L):
    for l in range(C):
        if M[k][l] == "#":
            x = mapnavio(k,l,L-1,C-1)
            jogo += x
print(jogo)
