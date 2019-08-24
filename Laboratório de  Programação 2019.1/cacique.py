class conjunto:
    def __init__(self, vertices, pai):
        self.vertices = vertices
        self.pai = pai

    def find(self, item):
        if self.pai[item] == item:
            return item
        else:
            return self.find(self.pai[item])

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.pai[root1] = root2

def mergeSort(lista):
    global inter
    if len(lista) == 1:
        return lista
    metade = int(len(lista) / 2)
    listaEsquerda = lista[:metade]
    listaDireita = lista[metade:]
    listaNova = []
    listaEsquerda = mergeSort(listaEsquerda)
    listaDireita = mergeSort(listaDireita)

    i = 0
    j = 0
    while i < len(listaEsquerda) and j < len(listaDireita):
        if listaEsquerda[i] <= listaDireita[j]:
            listaNova.append(listaEsquerda[i])
            i += 1
        else:
            listaNova.append(listaDireita[j])
            j += 1

    listaNova += listaEsquerda[i:] + listaDireita[j:]    

    return listaNova

imprimir = ""
contador = 0
while True:
    entrada = input()
    try:
        if int(entrada) == 0:
            break
    except:
        N, arestas = list(map(int, entrada.split()))
        contador += 1
        vertices = []
        verticesConj = [i+1 for i in range(N)]
        representante = {}
        for v in verticesConj:
            representante[v] = v

        dj = conjunto(verticesConj,representante)

        for i in range(arestas):
            u, v, p = list(map(int, input().split()))
            vertices.append((p,u,v))
            vertices.append((p,v,u))

        arvore_minima = []
        arestas_ordenadas = mergeSort(vertices)

        for a in arestas_ordenadas:
            if dj.find(a[1]) != dj.find(a[2]):
                dj.union(a[1],a[2])
                arvore_minima.append((a[1],a[2]))

        resultado = mergeSort(arvore_minima)
        
        parcial = ''

        for i in resultado:
            parcial += str([i][0][0]) + " " + str([i][0][1]) + "\n"
        imprimir += "Teste " + str(contador) + "\n" + parcial + " \n"

print(imprimir)