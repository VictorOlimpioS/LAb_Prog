class No:
    def __init__(self, dado, prox=None, ant=None):
        self._dado = dado
        self._prox = prox
        self._ant = ant

    def getDado(self):
        return self._dado

    def setDado(self, dado):
        self._dado = dado

    def getProx(self):
        return self._prox

    def setProx(self, prox):
        self._prox = prox

    def getAnt(self):
        return self._ant

    def setAnt(self, ant):
        self._ant = ant

class ListaDuplamenteEncadeada:

    def __init__(self, inicio=None):
        self._inicio = inicio

    def getInicio(self):
        return self._inicio

    def setInicio(self, inicio):
        self._inicio = inicio

    def isVazia(self):
        return self._inicio == None

    def inserirNoInicio(self, dado):
        novono = No(dado)
        if not self.isVazia():
            novono.setProx(self._inicio)
            self._inicio.setAnt(novono)
        self._inicio = novono

   
    def removerOMenor(self, distancia):
        if not self.isVazia():
            i = self._inicio
            menor = float('inf')
            while i is not None:
                if distancia[i.getDado()] < menor:
                    menor = distancia[i.getDado()]
                    menorNo = i
                i = i.getProx()
            if menorNo is not None:
                if menorNo.getProx() is not None:
                    menorNo.getProx().setAnt(menorNo.getAnt())
                if menorNo.getAnt() is not None:
                    menorNo.getAnt().setProx(menorNo.getProx())
                if menorNo is self._inicio:
                    self._inicio = menorNo.getProx()
                return menorNo.getDado()
        return -1

    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado()) + ", "
            i = i.getProx()
        return s




def dijkstra(G, origem,N):
    Q = ListaDuplamenteEncadeada()
    dist = [float('Inf')]*N
    for u in range(N):
        Q.inserirNoInicio(u)
    dist[origem-1] = 0

    while not Q.isVazia():
        u = Q.removerOMenor(dist)
        for v, p in G[u]:
            pesoNovoCaminho = dist[u] + p
            if pesoNovoCaminho < dist[v]:
                dist[v] = pesoNovoCaminho
    return(dist)

def maior(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i 
    return maior


N, arestas = list(map(int, input().split()))
vertices = [[] for i in range(N)]
elementos = [i+1 for i in range(N)]
      
for i in range(arestas):
    u, v, p = list(map(int, input().split()))
    vertices[u-1].append((v-1, p))
    vertices[v-1].append((u-1, p))
            
Cr = float("inf")
Rs = ''
melhor = None
for i in elementos:
    melhor = dijkstra(vertices,i,N)
    C = maior(melhor)
    if C < Cr:
        Cr = C
    
print(Cr)