class No:
    def __init__(self,dado):
        self.__dado = dado
        self.__prox = None
        self.__ant = None
    def getDado(self):
        return self.__dado
    def getProx(self):
        return self.__prox
    def getAnt(self):
        return self.__ant
    def setDado(self,dado):
        self.__dado = dado
    def setProx(self,prox):
        self.__prox = prox
    def setAnt(self,ant):
        self.__ant = ant

class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._fim = None
    def getInicio(self):
        return self._inicio
    def getFim(self):
        return self._fim
    def setInicio(self,inicio):
        self._inicio = inicio
    def setFim(self,fim):
        self._fim = fim

    def buscar(self,dado):
        i = self._inicio
        while i is not None:
            if i.getDado() == dado:
                return i
            i = i.getProx()
        return i #não achou

    def isVazia(self):
        return self._inicio is None

    def tamanhoLista(self):
        i = self._inicio
        tamanho = 0
        if self.isVazia():
            return 0
        else:
            while i is not None:
                tamanho += 1
                i = i.getProx()
        return tamanho

    def inserirNoInicio(self,dado):
        novoNo = No(dado)
        if self.isVazia():
            self._inicio = novoNo
            self._fim = self._inicio
        else:
            novoNo.setProx(self._inicio)
            self._inicio.setAnt(novoNo)
            self._inicio = novoNo

    def inserirNoFim(self,dado):
        novoNo = No(dado)
        if self.isVazia():
            self._inicio = novoNo
            self._fim = self._inicio
        else:
            novoNo.setAnt(self._fim)
            self._fim.setProx(novoNo)
            self._fim = novoNo

    def removerDado(self,dado):
        noRemovido = self.buscar(dado)
        if noRemovido is not None:
            prox = noRemovido.getProx()
            ant = noRemovido.getAnt()
            if self._inicio is self._fim:
               self._inicio = self._fim = None
            elif noRemovido is self._inicio:
                prox.setAnt(None)
                self._inicio = prox
            elif noRemovido is self._fim:
                ant.setProx(None)
                self._fim = ant
        return noRemovido
    def removerInicio(self):
        no = self._inicio
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._inicio.getProx().setAnt(None)
                self._inicio = self._inicio.getProx()
            else:
                self._incio = self._fim = None
        return no

    def removerDoFim(self):
        i = self._fim
        if not self.isVazia():
            if self._inicio is not self._fim:
                self._fim.getAnt().setProx(None)
                self._fim = self._fim.getAnt()
            else:
                self._inicio = self._fim = None

    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado()) + '|'
            i = i.getProx()
        if s is "":
            s = "Lista vazia"
        return s
class Fila(ListaEncadeada):

    def inserir(self,dado):
        super().inserirNoFim(dado)

    def remover(self):
        return super().removerInicio()

    def esvaziaFila(self):
        self._inicio = self._fim = None

    def retorna(self):
        return super().removerInicio().getDado()

    def tamanhoDaFila(self):
        return super().tamanhoLista()


    def __str__(self):
        s = ""
        i = self._inicio
        while i is not None:
            s += str(i.getDado())
            i = i.getProx()
            if i is not None:
                s += "->"
        if s is "":
            return "Fila vazia"
        return "Primeiro a chegar "+s+"-> Último a chegar"


festas = int(input())

for i in range(festas):
    jogadores = []
    while True:
        jogos = input()
        deck = Fila()
        if jogos == "-1":
            break
        for j in jogos:
            try:
                deck. inserir(int(j))
            except:
                continue
        jogadores.append(deck)
    tempMesa = None
    tempJogador = None
    flag = False
    winner = None
    contador = 0
    while contador < 1001:
        topo = jogadores[0].getInicio().getDado()
        for m in range(1,len(jogadores)):
            if jogadores[m].isVazia():
                flag = True
                winner = m
                break
            elif jogadores[m].getInicio().getDado() == topo:
                if jogadores[m].tamanhoDaFila() == 1:
                    jogadores[m].esvaziaFila()
                    flag = True
                    winner = m
                    break
                else:
                    jogadores[m].remover()
                    if jogadores[m].isVazia():
                        flag = True
                        winner = m
                        break

            elif jogadores[m].getInicio().getDado() != topo:
                if jogadores[m].tamanhoDaFila() == 1:
                    pass
                else:
                    tempJogador = jogadores[m].getInicio().getDado()
                    jogadores[m].remover()
                    jogadores[m].inserir(tempJogador)

        tempMesa = jogadores[0].getInicio().getDado()
        jogadores[0].remover()
        jogadores[0].inserirNoFim(tempMesa)
        contador += 1
        if flag == True:
            if i == festas -1:
                print(str(winner)+"\n" )
                break
            else:
                print(winner)
                break
        if contador == 1000:
            if i == festas -1:
                print(str(0)+"\n")
                break
            else:
                print(0)
                break















