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
            inter += (len(listaEsquerda) - i)
            j += 1

    listaNova += listaEsquerda[i:] + listaDireita[j:]    

    return listaNova
     
inter = 0
num = int(input())
lista = [int(x) for x in input().split()]
mergeSort(lista)
print(inter)