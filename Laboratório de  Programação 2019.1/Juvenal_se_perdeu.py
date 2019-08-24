class No:
    def __init__(self,dado):
        self._dado = dado
        self._pai = None
        self._esquerdo = None
        self._direito = None
    
    def getDado(self):
        return self._dado
    def getPai(self):
        return self._pai
    def getEsquerdo(self):
        return self._esquerdo
    def getDireito(self):
        return self._direito
    
    def setDado(self,dado):
        self._dado = dado
    def setPai(self,pai):
        self._pai = pai
    def setEsquerdo(self,esquerdo):
        self._esquerdo = esquerdo
    def setDireito(self,direito):
        self._direito = direito
    
    def __str__(self):
        return str(self._dado)

class ArvoreBinariaBusca:
    def __init__(self):
        self._raiz = None
    
    def getRaiz(self):
        return self._raiz
    
    def setRaiz(self,novaRaiz):
        self._raiz = novaRaiz

    def isVazia(self):
        return self._raiz is None

    def inserir(self,dado):
            z = No(dado)
            pai = None
            x = self.getRaiz()
            while x != None:
                  pai = x
                  if dado > x.getDado():
                        x = x.getDireito()
                  else:
                        x = x.getEsquerdo()
            z.setPai(pai)
            if pai == None:
                  self.setRaiz(z)
            else:
                  if dado > pai.getDado():
                        pai.setDireito(z)
                  else:
                        pai.setEsquerdo(z)
    
    def isVazia(self):
        if self._raiz is None:
            return True

    def isFilhoEsq(self,no):
        if no is not None:
            if no is not self._raiz:
                return no is no.getPai().getEsquerdo()
        return False
    
    def isFilhoDir(self,no):
        if no is not None:
            if no is not self._raiz:
                return no is no.getPai().getDireito()
        return False
        

    def remover(self,z):
            if z.getEsquerdo() == None or z.getDireito() == None:
                  y=z
            else:
                  y = self.sucessor(z)

            if y.getEsquerdo() != None:
                  x = y.getEsquerdo()
            else:
                  x = y.getDireito()

            if x != None:
                  x.setPai(y.getPai())

            if y.getPai == None:
                  self._raiz = x

            else:
                  if y == y.getPai().getEsquerdo():
                        y.getPai().setEsquerdo(x)
                  else:
                        y.getPai().setDireito(x)
            if y!=z:
                  z.setDado(y.getDado())
            return y
    
    def altura(self,no):
        if no is None:
            return 0
        else:
            EsquAltura = self.altura(no.getEsquerdo())
            DirAltura = self.altura(no.getDireito())
        if EsquAltura > DirAltura:
            return EsquAltura + 1
        else:
            return DirAltura + 1


    def buscar(self,no,dado):
        if no is None or dado == no.getDado():
            return no
        else:
            if dado < no.getDado():
                return self.buscar(no.getEsquerdo(),dado)
            else:
                return self.buscar(no.getDireito(),dado)
    
    def busca_largura(self,dado):
        fila = [self._raiz]
        if self._raiz == None:
            return None
        while True:
            if len(fila) != 0:
                compara = fila.pop(0)
            else:
                return 0
            if compara.getDado() == dado:
                return compara
            else:
                if compara.getEsquerdo() is not None:
                    fila.append(compara.getEsquerdo())
                if compara.getDireito() is not None:
                    fila.append(compara.getDireito())

    
    def minimo(self,no):
        while no.getEsquerdo() is not None:
            no = no.getEsquerdo()
        return no
            
    def maximo(self,no):
        while no.getDireito() is not None:
            no = no.getDireito()
        return no
            
    def sucessor(self,no):
        if no is None:
            return None
        if no.getDireito() is not None:
            return self.minimo(no.getDireito())
        else:
            pai = no.getPai()
            while pai is not None and no == pai.getDireito():
                no = pai
                pai = pai.getPai()
            return pai 
    
    def metodoC(self,no):
        global resultado
        global dado
        if no is not None:
            self.metodoC(no.getEsquerdo())
            if no.getDado() < dado:
                resultado = no.getDado()
            self.metodoC(no.getDireito())
        else:
            pass
        return resultado

    def antecessor(self,no):
        if no is None:
            return None
        if no.getEsquerdo() is not None:
            return self.maximo(no.getEsquerdo())
        else:
            pai = no.getPai()
            while pai is not None and no == pai.getEsquerdo():
                no = pai
                pai = pai.getPai()
            return pai 


    def inOrdem(self,no):
        global res
        if no == None:
            pass
        else:
            self.inOrdem(no.getEsquerdo())
            res += str(no.getDado()) + " "
            self.inOrdem(no.getDireito())
    
    def preOrdem(self,no):
        global res
        if no == None:
            pass
        else:
            res += str(no.getDado()) + " "
            self.preOrdem(no.getEsquerdo())
            self.preOrdem(no.getDireito())

    def posOrdem(self,no):
        global res
        if no == None:
            pass
        else:
            self.posOrdem(no.getEsquerdo())
            self.posOrdem(no.getDireito())
            res += str(no.getDado()) +" "
contador = 1
resultado = 0
total = ""
while True:
    try:
        arvore = ArvoreBinariaBusca()
        x = input().split()
        OP = int(x[0])
        resposta = ""
        for i in range(OP):
            opr = input().split()
            parcial = ""
            if opr[0] == "A":
                arvore.inserir(int(opr[1]))
            elif opr[0] == "B":
                no = arvore.busca_largura(int(opr[1]))
                if no == 0:
                    resposta += "0\n"
                else:
                    arvore.remover(no)
            elif opr[0] == "C":
                dado = int(opr[1])
                
                maioMenor = arvore.metodoC(arvore.getRaiz())
                resposta += str(maioMenor) + "\n"
            elif opr[0] == "PRE":
                if arvore.isVazia():
                    resposta += "0\n"
                else:
                    res = ""
                    arvore.preOrdem(arvore.getRaiz())
                    resposta += str(res[:-1]) + "\n"
            elif opr[0] == "IN":
                if arvore.isVazia():
                    resposta += "0\n"
                else:
                    res = ""
                    arvore.inOrdem(arvore.getRaiz())
                    resposta += str(res[:-1]) + "\n"
            elif opr[0] == "POST":
                if arvore.isVazia():
                    resposta += "0\n"
                else:
                    res = ""
                    arvore.posOrdem(arvore.getRaiz())
                    resposta += str(res[:-1]) + "\n"
        parcial += "Caso " + str(contador) + ":\n" + resposta 
        contador += 1  
        total += parcial
    except:
        break
print(total)     





    
