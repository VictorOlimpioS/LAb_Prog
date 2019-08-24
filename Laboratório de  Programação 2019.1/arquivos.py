entrada = input()
Bytes, limite = list(map(int, entrada.split()))
arquivos = input()
lista = list(map(int, arquivos.split()))

def mergeSort(lista):
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

listaOrdem = mergeSort(lista)

ultimo = Bytes-1
marcador = [False for i in range(Bytes)]
resultado = Bytes

for i in range(Bytes):
    if marcador[i]:
        continue
    while ultimo >= 0 and listaOrdem[i] + listaOrdem[ultimo] > limite:
        ultimo -= 1
    
    if ultimo >  i :
        marcador[ultimo] = True
        marcador[i] = True
        resultado -= 1
        if listaOrdem[i] + listaOrdem[ultimo] <= limite:
            ultimo -= 1 
   


print (resultado)
