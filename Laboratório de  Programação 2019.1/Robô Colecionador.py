while True:       #Laço repetitivo para garantir o cáculo de todos os casos
    L, C, nI = map(int, input().split()) #recebendo o tamanho da Matris dos robôs (Linha e coluna) e o número de interações
    if L == 0 and C == 0 and nI == 0:
        break
    else:
        M = []
        Fig = 0 # Ponteiro para a coleta das figurinhas
        for i in range(L): #Montando a Matriz
            matriz = input()
            matriz = list(matriz)
            M.append(matriz)
        S = ' '.join(input()).split() #recebendo as instruções

        for i in range(L): #Laço feito para encontrar a posição inicial do robô
            marcador = True
            for j in range(C):
                if M[i][j] == "N":
                    PosRB = [i, j, M[i][j]] # PosRB = Posição do robô ; [Linha, Coluna, Orientação]
                    marcador = False # marcador para quebra do laço quando se encontra a posição
                    break
                elif M[i][j] == "S":
                    PosRB = [i, j, M[i][j]]
                    marcador = False
                    break
                elif M[i][j] == "L":
                    PosRB = [i, j, M[i][j]]
                    marcador = False
                    break
                elif M[i][j] == "O":
                    PosRB = [i, j, M[i][j]]
                    marcador = False
                    break
            if marcador == False:
                break
        for k in range(nI): #Sequência de comandos para os movimentos rotacionais
            if S[k] == "D": #Virar a direita
                if PosRB[2] == "N":
                    PosRB[2] = "L"
                    M[PosRB[0]][PosRB[1]] = "L"
                elif PosRB[2] == "S":
                    PosRB[2] = "O"
                    M[PosRB[0]][PosRB[1]] = "O"
                elif PosRB[2] == "L":
                    PosRB[2] = "S"
                    M[PosRB[0]][PosRB[1]] = "S"
                elif PosRB[2] == "O":
                    PosRB[2] = "N"
                    M[PosRB[0]][PosRB[1]] = "N"

            elif S[k] == "E": # Virar a esquerda
                if PosRB[2] == "N":
                    PosRB[2] = "O"
                    M[PosRB[0]][PosRB[1]] = "O"
                elif PosRB[2] == "S":
                    PosRB[2] = "L"
                    M[PosRB[0]][PosRB[1]] = "L"
                elif PosRB[2] == "L":
                    PosRB[2] = "N"
                    M[PosRB[0]][PosRB[1]] = "N"
                elif PosRB[2] == "O":
                    PosRB[2] = "S"
                    M[PosRB[0]][PosRB[1]] = "S"
                    t = M[PosRB[0]][1]

            elif S[k] == "F": # Sequência de comandos para o robô andar em frente com a interação com Pilastra, Figurinha e espaço livre.
                if PosRB[2] == "N":
                    if PosRB[0] - 1 >= 0:
                        if M[PosRB[0] - 1][PosRB[1]] == "#":  # Quando econtra-se uma pilastra não se pode andar
                            pass
                        elif M[PosRB[0] - 1][PosRB[1]] == "*": # se encontrar uma figurinha, ela é coletada, atualiza-se o ponteiro das figirinhas
                            Fig += 1
                            PosRB[0] -= 1                      #Atualiza-se a posição do robô no marcador da posição, como também na Matriz
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0] + 1][PosRB[1]] = "."     #É atualizada tbm a posição anterior que o robô estava
                        elif M[PosRB[0] - 1][PosRB[1]] == ".":
                            PosRB[0] -= 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0] + 1][PosRB[1]] = "."


                elif PosRB[2] == "S":
                    if PosRB[0] + 1 <= L - 1:
                        if M[PosRB[0] + 1][PosRB[1]] == "#":
                            pass
                        elif M[PosRB[0] + 1][PosRB[1]] == "*":
                            Fig += 1
                            PosRB[0] += 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0] - 1][PosRB[1]] = "."
                        elif M[PosRB[0] + 1][PosRB[1]] == ".":
                            PosRB[0] += 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0] - 1][PosRB[1]] = "."
                    else:
                        pass

                elif PosRB[2] == "L":
                    if PosRB[1] + 1 <= C - 1:
                        if M[PosRB[0]][(PosRB[1]) + 1] == "#":
                            pass
                        elif M[PosRB[0]][PosRB[1] + 1] == "*":
                            Fig += 1
                            PosRB[1] += 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0]][PosRB[1] - 1] = "."
                        elif M[PosRB[0]][PosRB[1] + 1] == ".":
                            PosRB[1] += 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0]][PosRB[1] - 1] = "."
                    else:
                        pass
                elif PosRB[2] == "O":
                    if PosRB[1] - 1 >= 0:
                        if M[PosRB[0]][PosRB[1] - 1] == "#":
                            pass
                        elif M[PosRB[0]][PosRB[1] - 1] == "*":
                            Fig += 1
                            PosRB[1] -= 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0]][PosRB[1] + 1] = "."
                        elif M[PosRB[0]][PosRB[1] - 1] == ".":
                            PosRB[1] -= 1
                            M[PosRB[0]][PosRB[1]] = PosRB[2]
                            M[PosRB[0]][PosRB[1] + 1] = "."
                    else:
                        pass

        print(Fig) #devolvendo o número de figurinhas