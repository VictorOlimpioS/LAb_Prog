vertices,origem,destino = map(int,input().split())
G = [[0 for i in range(vertices)]for j in range(vertices)]
marcador = [False for i in range(vertices)]
for i in range(vertices-1):
    a,b = [int(i) for i in input().split()]
    G[a-1][b-1] = 1
    G[b-1][a-1] = 1
custo = 0
resultado = 0

def solve(origem,custoo,marcador,destino):
    busca = [(origem,custoo,marcador)]
    while True:
        ponto,passo,flag = busca.pop(0)
        for i in range(vertices):
            if G[ponto-1][i] == 1:
                if i+1 == destino:
                    return passo+1
                if flag[i] == False:
                    marcador[ponto-1] = True
                    busca.append((i+1,passo+1,marcador))
                    

print(solve(origem,custo,marcador,destino))
