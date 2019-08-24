class No:
    def __init__(self,dado):
        self._dado = dado
        self._pai = None
        self._esquerdo = None
        self._direito = None
        self._altura = -1
        self._nivel = 1
    
    def getDado(self):
        return self._dado
    def getPai(self):
        return self._pai
    def getEsquerdo(self):
        return self._esquerdo
    def getDireito(self):
        return self._direito
    def getAltura(self):
        return self._altura
    def getNivel(self):
        return self._nivel
    
    def setDado(self,dado):
        self._dado = dado
    def setPai(self,pai):
        self._pai = pai
    def setEsquerdo(self,esquerdo):
        self._esquerdo = esquerdo
    def setDireito(self,direito):
        self._direito = direito
    def setAltura(self,altura):
        self._altura = altura
    def setNivel(self,nivel):
        self._nivel = nivel

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
                  z.setNivel(1)
            else:
                  if dado > pai.getDado():
                        pai.setDireito(z)
                  else:
                        pai.setEsquerdo(z)

            return z
            
    
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

class AVL(ArvoreBinariaBusca):

    def inserirAVL(self,dado):
        Noh = super().inserir(dado)
        self.definirAltura(self.getRaiz())
        while Noh is not None:
            self.balancear(Noh)
            Noh = Noh.getPai()
           

    def FatorDeBalanceamento(self,no):
        if no == None:
            pass
        if no.getEsquerdo() is None:
            e = -1
        else:
            e = no.getEsquerdo().getAltura()
        if no.getDireito() is None:
            d = -1
        else:
            d = no.getDireito().getAltura()
        return d-e
    
    def balancear(self,no):
        f = self.FatorDeBalanceamento(no)
        if f == 2 :
            if self.FatorDeBalanceamento(no.getDireito()) == 1:
                self.rotEsquerda(no)
                self.definirAltura(self.getRaiz())
            elif self.FatorDeBalanceamento(no.getDireito()) == -1:
                self.rotDuplaEsquerda(no)
                self.definirAltura(self.getRaiz())
        elif f == -2:
            if self.FatorDeBalanceamento(no.getEsquerdo()) == -1:
                self.rotDireita(no)
                self.definirAltura(self.getRaiz())
            elif self.FatorDeBalanceamento(no.getEsquerdo()) == 1:
                self.rotDuplaDireita(no)
                self.definirAltura(self.getRaiz())


    def rotEsquerda(self, x):
        y = x.getDireito()
        x.setDireito(y.getEsquerdo())
        if x.getEsquerdo() is not None:
            y.getEsquerdo().setPai(x)
        y.setPai(x.getPai())
        if x.getPai() is None:
           self.setRaiz(y)
        elif x == x.getPai().getEsquerdo():
            x.getPai().setEsquerdo(y)
        else:
            x.getPai().setDireito(y)      
        y.setEsquerdo(x)
        x.setPai(y)

    def rotDireita(self,y):
        x = y.getEsquerdo()
        y.setEsquerdo(x.getDireito())
        if x.getDireito() is not None:
            x.getDireito().setPai(y)
        x.setPai(y.getPai())
        if y.getPai() is None:
           self.setRaiz(x)
        elif y == y.getPai().getDireito():
            y.getPai().setDireito(x)
        else:
            y.getPai().setEsquerdo(x)      
        x.setDireito(y)
        y.setPai(x)
        
    def rotDuplaEsquerda(self,no):
        self.rotDireita(no.getDireito())
        self.rotEsquerda(no)

    def rotDuplaDireita(self,no):
        self.rotEsquerda(no.getEsquerdo())
        self.rotDireita(no)
        

    def definirAltura(self,no):
        if no is not None:
            d = self.definirAltura(no.getDireito())
            e = self.definirAltura(no.getEsquerdo())
            no.setAltura(1 + max(d,e))
            return 1 + max(d,e)
        return -1
    
    def buscarNivel(self,no):
        fila = [self._raiz]
        if self._raiz == None:
            return None
        while True:
            if len(fila) != 0:
                compara = fila.pop(0)
                if compara.getPai() == None:
                    compara.setNivel(1)
                else:
                    compara.setNivel(compara.getPai().getNivel() + 1)
            else:
                return -1
            if compara.getDado() == no:
                return compara.getNivel()
            else:
                if compara.getEsquerdo() is not None:
                    fila.append(compara.getEsquerdo())
                if compara.getDireito() is not None:
                    fila.append(compara.getDireito())
    
    def printFilmes(self,n1,n2,no):
        global res
        if no == None:
            pass
        else:
            self.printFilmes(n1,n2,no.getEsquerdo())
            if no.getDado() >= n1 and no.getDado() <= n2:
                res += str(no.getDado()) + " "
            else:
                pass
            self.printFilmes(n1,n2,no.getDireito())
        if res == '':
            return "-1"
        else:
            return res[:-1]


