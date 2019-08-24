while True:
    try:
        a, b, = [int(x) for x in input().split()] #Tratando a entrada para o número de dígitos e dos números a serem retirados
        dgt = [int(x) for x in ' '.join(input()).split()] #Recebendo os dígitos

        for i in range(b): #Laço de acordo com o número de dígitos a serem retirados
            marcador = True #Adiconando um marcador para a indicar a retirada de um elemento e voltar para o laço de fora
            for j in range(a-1):
                if dgt[j] < dgt[j+1]: #checkando se o sucessor de j é maior que ele para assim retirá-lo
                    del dgt[j] #removendo um dígito
                    marcador = False #setando o marcador
                    a -= 1 #atualizando a lista de dígitos
                    break
                else:
                    pass
            if marcador:
                del dgt[-1]#removendo um dígito
                a -= 1

        print(''.join(map(str, dgt))) #printando a sequência de dígitos

    except EOFError:
        break