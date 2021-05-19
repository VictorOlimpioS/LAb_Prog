// Projeto de Sistema para Biblioteca desenvolvido em Python com estrutura de árvores vermelha e preta e orientação à objeto

class Nodo():

    def __init__(self, registro):
        self.dado = registro
        self.pai = None
        self.left = None
        self.right = None
        self.cor = None


class Nodo_livro():

    def __init__(self, nome, registro):
        self.dado = registro
        self.pai = None
        self.left = None
        self.right = None
        self.cor = None
        self.emprestado = False
        self.reservado = False
        self.data = None

        self.nome = nome
        self.reserva = []


class Nodo_aluno():
    def __init__(self, nome, registro):
        self.dado = registro
        self.pai = None
        self.left = None
        self.right = None
        self.cor = None
        self.data = None
        self.multa = None

        self.nome = nome
        self.livros_atuais = []


class Arvore():

    def __init__(self):
        self.vazio = Nodo(None)
        self.vazio.cor = "black"
        self.vazio.pai = self.vazio
        self.vazio.left = self.vazio
        self.vazio.right = self.vazio
        self.raiz = self.vazio

    def procurar(self, n):
        raiz = self.raiz
        while raiz != self.vazio and n != raiz.dado:
            if n < raiz.dado:
                raiz = raiz.left
            else:
                raiz = raiz.right
        return raiz

    def minimo(self, nodo):
        if nodo != self.vazio:
            while nodo.left != self.vazio:
                nodo = nodo.left
            return nodo

    def maximo(self, nodo):
        if nodo != self.vazio:
            while nodo.right != self.vazio:
                nodo = nodo.right
            return nodo

    def predecessor(self, x):
        if x != self.vazio:
            return self.maximo(x.left)
        y = x.pai
        while y != self.vazio and x == y.left:
            x = y
            y = y.pai
        return y

    def sucessor(self, x):
        if x != self.vazio:
            return self.minimo(x.right)

        y = x.pai

        while y != self.vazio and x == y.right:
            x = y
            y = y.pai
        return y

    def em_ordem(self, nodo):
        if nodo != self.vazio:
            self.em_ordem(nodo.left)
            print(nodo.dado,nodo.nome)
            self.em_ordem(nodo.right)

    def rodar_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.vazio:
            y.left.pai = x
        y.pai = x.pai

        if x.pai == self.vazio:
            self.raiz = y
        elif x == x.pai.left:
            x.pai.left = y
        else:
            x.pai.right = y
        y.left = x
        x.pai = y

    def rodar_right(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.vazio:
            y.right.pai = x
        y.pai = x.pai

        if x.pai == self.vazio:
            self.raiz = y
        elif x == x.pai.right:
            x.pai.right = y
        else:
            x.pai.left = y
        y.right = x
        x.pai = y

    def rb_inserir(self, z):

        while z.pai.cor == "red":
            if z.pai == z.pai.pai.left:
                y = z.pai.pai.right
                if y.cor == "red":
                    z.pai.cor = "black"
                    y.cor = "black"
                    z.pai.pai.cor = "red"
                    z = z.pai.pai
                else:
                    if z == z.pai.right:
                        z = z.pai
                        self.rodar_left(z)
                    z.pai.cor = "black"
                    z.pai.pai.cor = "red"
                    self.rodar_right(z.pai.pai)
            else:
                y = z.pai.pai.left
                if y.cor == "red":
                    z.pai.cor = "black"
                    y.cor = "black"
                    z.pai.pai.cor = "red"
                    z = z.pai.pai
                else:
                    if z == z.pai.left:
                        z = z.pai
                        self.rodar_right(z)
                    z.pai.cor = "black"
                    z.pai.pai.cor = "red"
                    self.rodar_left(z.pai.pai)
        self.raiz.cor = "black"

    def rb_trans(self, u, v):
        if u.pai == self.vazio:
            self.raiz = v
        elif u == u.pai.left:
            u.pai.left = v
        else:
            u.pai.right = v
        v.pai = u.pai

    def inserir(self, novo):
        y = self.vazio
        x = self.raiz

        while x != self.vazio:
            y = x
            if novo.dado < x.dado:
                x = x.left
            elif novo.dado > x.dado:
                x = x.right
            else:
                print("ID já cadastrado")
                return
        novo.pai = y

        if y == self.vazio:
            self.raiz = novo

        elif novo.dado < y.dado:
            y.left = novo

        else:
            y.right = novo
        novo.left = self.vazio
        novo.right = self.vazio
        novo.cor = "red"
        self.rb_inserir(novo)
        print("Cadastro realizado")

    def remover(self, z):
        y = z
        y_original_cor = z.cor
        if z.left == self.vazio:
            x = z.right
            self.rb_trans(z, z.right)
        elif z.right == self.vazio:
            x = z.left
            self.rb_trans(z, z.left)
        else:
            y = self.minimo(z.right)
            y_original_cor = y.cor
            x = y.right
            if y.pai == z:
                x.pai = y
            else:
                self.rb_trans(y, y.right)
                y.right = z.right
                y.right.pai = y
            self.rb_trans(z, y)
            y.left = z.left
            y.left.pai = y
            y.cor = z.cor
        if y_original_cor == "black":
            self.rb_remover(x)

    def rb_remover(self, x):
        while x != self.raiz and x.cor == "black":
            if x == x.pai.left:
                w = x.pai.right
                if w.cor == "red":
                    w.cor = "black"
                    x.pai.cor = "red"
                    self.rodar_left(x.pai)
                    w = x.pai.right
                if w.left.cor == "black" and w.right.cor == "black":
                    w.cor = "red"
                    x = x.pai
                else:
                    if w.right.cor == "black":
                        w.left.cor = "black"
                        w.cor = "red"
                        self.rodar_right(w)
                        w = x.pai.right
                    w.cor = x.pai.cor
                    x.pai.cor = "black"
                    w.right.cor = "black"
                    self.rodar_left(x.pai)
                    x = self.raiz

            else:
                w = x.pai.left
                if w.cor == "red":
                    w.cor = "black"
                    x.pai.cor = "red"
                    self.rodar_right(x.pai)
                    w = x.pai.left
                if w.right.cor == "black" and w.left.cor == "black":
                    w.cor = "red"
                    x = x.pai
                else:
                    if w.left.cor == "black":
                        w.right.cor = "black"
                        w.cor = "red"
                        self.rodar_left(w)
                        w = x.pai.left
                    w.cor = x.pai.cor
                    x.pai.cor = "black"
                    w.left.cor = "black"
                    self.rodar_right(x.pai)
                    x = self.raiz
        x.cor = "black"



from datetime import date


alunos = Arvore()
livros = Arvore()

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return (valor)
        except ValueError:
            print("Valor inválido, favor digitar entre %d e %d" % (inicio, fim))

def data():
    hoje = date.today()
    futuro = date.fromordinal(hoje.toordinal() +5)
    dia = str(futuro.day)
    mes = str(futuro.month)
    ano = str(futuro.year)
    if len(dia) == 1:
        dia = "0" + dia
    if len(mes) == 1:
        mes = "0" + mes
    return("%s-%s-%s" % (dia, mes, ano))


def multa(passado):
    hoje = date.today()
    passadoSplit = passado.split("-")
    dia = int(passadoSplit[0])
    mes = int(passadoSplit[1])
    ano = int(passadoSplit[2])
    passadoDate = date(ano,mes,dia)
    multa = hoje.toordinal() - passadoDate.toordinal()
    return multa



def menu():
    print("""
1  - Cadastrar aluno
2  - Cadastrar livro
3  - Remover aluno
4  - Remover livro
5  - Consultar aluno
6  - Consultar livro
7  - Emprestimo de livro
8  - Devolução
9  - Pagar multa
10 - Consultar multa
11 - Listar todos os alunos
12 - Listar todos os livros


0  - Sair
""")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 12)


while True:

    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        nome = input("Digite o nome do aluno: ")
        registro = int(input("Digite o numero do CPF: "))
        alunos.inserir(Nodo_aluno(nome, registro))
    elif opção == 2:
        nome = input("Digite o nome do livro: ")
        registro = int(input("Digite o numero do ID do livro: "))
        livros.inserir(Nodo_livro(nome, registro))
    elif opção == 3:
        remover = int(input("Digite o CPF do aluno a ser removido: "))
        elemento = alunos.procurar(remover)
        if elemento != alunos.vazio:
            alunos.remover(elemento)
            print("Aluno removido com sucesso")
        else:
            print("Aluno não encontrado")

    elif opção == 4:
        remover = int(input("Digite o ID do livro a ser removido: "))
        elemento = livros.procurar(remover)
        if elemento != livros.vazio:
            livros.remover(elemento)
            print("Livro removido com sucesso")
        else:
            print("Livro não encontrado")

    elif opção == 5:
        consultar = int(input("Digite o CPF: "))
        elemento = alunos.procurar(consultar)
        if elemento != alunos.vazio:
            if len(elemento.livros_atuais) == 0:
                print("ID: %d\nAluno: %s" % (elemento.dado,elemento.nome))
            else:
                titulo, id = elemento.livros_atuais[0]
                print("ID: %d\nAluno: %s\nLivro : %s ID: %d\nData de devolução: %s" % (elemento.dado,elemento.nome,titulo,id,elemento.data))
        else:
            print("Aluno não encontrado")

    elif opção == 6:
        consulta = int(input("Digite o ID do livro: "))
        elemento = livros.procurar(consulta)
        if elemento != livros.vazio:
            print("ID: %d\nTitulo: %s" % (elemento.dado,elemento.nome))
        else:
            print("Livro não encontrado")

    elif opção == 7:
        aluno = int(input("Numero do CPF do aluno a ser emprestado o livro: "))
        buscar_aluno = alunos.procurar(aluno)
        if buscar_aluno != alunos.vazio:
            if len(buscar_aluno.livros_atuais) >= 1:
                print("Limite de empréstimos excedido")

            elif buscar_aluno.multa != None and buscar_aluno.multa > 0:
                print("Aluno caloteiro\nMulta : R$ %d" % buscar_aluno.multa)

            else:
                livro = int(input("Numero do ID do livro: "))
                buscar_livro = livros.procurar(livro)
                if buscar_livro != livros.vazio:
                    if buscar_livro.emprestado:
                        if buscar_livro.reservado:
                            if buscar_livro.reserva[0] == buscar_aluno.dado:
                                print("Livro ainda está emprestado, aguarde a devolução")
                            else:
                                print("Livro já está emprestado e reservado")
                        else:
                            reserva = input("Livro emprestado, reservar? Digite S ou N: ")
                            if reserva == "S":
                                buscar_livro.reservado = True
                                buscar_livro.reserva.append(buscar_aluno.dado)
                                print("Reserva realizada com sucesso")
                                print("Previsão para disponibilidade: %s" % (buscar_livro.data))
                            else:
                                pass
                    elif buscar_livro.reservado:
                        if buscar_livro.reserva[0] == buscar_aluno.dado:
                            buscar_livro.emprestado = True
                            buscar_aluno.livros_atuais.append((buscar_livro.nome, buscar_livro.dado))
                            horario = data()
                            buscar_aluno.data = horario
                            buscar_livro.data = horario
                            buscar_livro.reservado = False
                            buscar_livro.reserva = []
                            print("Empréstimo realizado com sucesso\nData de devolução: %s" % (horario))
                        else:
                            print("Aluno não corresponde a reserva")

                    else:
                        buscar_livro.emprestado = True
                        buscar_aluno.livros_atuais.append((buscar_livro.nome,buscar_livro.dado))
                        horario = data()
                        buscar_aluno.data = horario
                        buscar_livro.data = horario
                        print("Empréstimo realizado com sucesso\nData de devolução: %s" % (horario))
                else:
                    print("Livro não encontrado")
        else:
            print("Aluno não cadastrado")


    elif opção == 8:
        aluno = int(input("Digite o numero do CPF: "))
        buscar_aluno = alunos.procurar(aluno)
        if buscar_aluno == alunos.vazio:
            print("CPF inválido")
        else:
            livro = int(input("Digite o numero do ID do livro: "))
            buscar_livro = livros.procurar(livro)
            if buscar_livro == livros.vazio:
                print("ID inválido")
            else:
                if buscar_livro.emprestado:
                    if len(buscar_aluno.livros_atuais) == 1:
                        if buscar_aluno.livros_atuais[0][1] == livro:
                            buscar_livro.emprestado = False
                            buscar_aluno.livros_atuais = []
                            if multa(buscar_aluno.data) >= 0:
                                buscar_aluno.multa = multa(buscar_aluno.data)
                            print("Livro devolvido")
                            if buscar_aluno.multa != None and buscar_aluno.multa > 0:
                                print("Multa gerada no valor de: R$ %d" % buscar_aluno.multa)
                        else:
                            print("O ID do livro não confere com o CPF do aluno")
                    else:
                        print("O aluno não possui empréstimo")
                else:
                    print("Livro consultado não está emprestado")

    elif opção == 9:
        aluno = int(input("Digite o numero do CPF: "))
        buscar_aluno = alunos.procurar(aluno)
        if buscar_aluno == alunos.vazio:
            print("CPF inválido")
        else:
            if buscar_aluno.multa != None and buscar_aluno.multa != 0:
                print("Valor da multa: R$ %d" % buscar_aluno.multa)
                pagamento = int(input("Digite o valor a ser pago: "))
                buscar_aluno.multa -= pagamento
            else:
                print("Aluno não possui multa")

    elif opção == 10:
        aluno = int(input("Digite o numero do CPF: "))
        buscar_aluno = alunos.procurar(aluno)
        if buscar_aluno == alunos.vazio:
            print("CPF inválido")
        else:
            if buscar_aluno.multa != None and buscar_aluno.multa != 0:
                print("Valor da multa: R$ %d" % buscar_aluno.multa)
            else:
                print("Aluno não possui multa")

    elif opção == 11:
        alunos.em_ordem(alunos.raiz)

    elif opção == 12:
        livros.em_ordem(livros.raiz)
