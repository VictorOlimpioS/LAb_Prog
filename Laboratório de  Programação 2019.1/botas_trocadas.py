botas  = int(input())
pares = {}


def minimo(x,y):
    if x < y :
        return x 
    return y 

for i in range(botas):
    tamanho, pe  = input().split()
   
    try:
        if pe == "D":
            pares[int(tamanho)]["D"] += 1
        else:
            pares[int(tamanho)]["E"] += 1
            
    except:
        pares[int(tamanho)] = {"D":0,"E":0}
        if pe =="D":
            pares[int(tamanho)]["D"] += 1
        else:
            pares[int(tamanho)]["E"] += 1


resu = 0

for i in pares:
    resu += minimo(pares[i]["D"],pares[i]["E"])

print(resu)
