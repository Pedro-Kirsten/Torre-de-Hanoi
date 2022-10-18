from typing import List

print("*** TORRE DE HANOI ***")

discos = int(input("\nNúmero de discos: "))

torre1 = []
torre2 = []
torre3 = []

for i in range(1, discos + 1):
    torre1.append(i)


def movimento():
    MostrarTorres()
    origem = int(input("\nTorre de origem: "))
    if origem >= 1 and origem <= 3:
        destino = int(input("\nDestino: "))

        ## Se a torre de origem for 1
        if origem == 1:
            if len(torre1) != 0:
                mov_peca = int(input("Peça a ser movida: "))
                if destino == 2:
                    if len(torre2) == 0:
                        torre1.remove(mov_peca)
                        torre2.append(mov_peca)
                    else:
                        if torre1[-1] > torre2[-1]:
                            torre2.append(mov_peca)
                            torre1.remove(mov_peca)
                        else:
                            aviso_peca()
                if destino == 3:
                    if len(torre3) != 0:
                        torre3.append(mov_peca)
                        torre1.remove(mov_peca)
                    if len(torre3) == 0:
                        torre3.append(mov_peca)
                        torre1.remove(mov_peca)
                    else:
                        aviso_peca()
                else:
                    print("Torre de origem vazia.")

        ## Se a torre de origem for 2
        if origem == 2:
            if len(torre2) != 0:
                mov_peca = torre2[-1]
                torre2.remove(mov_peca)
                if destino == 1:
                    torre1.append(mov_peca)
                if destino == 3:
                    torre3.append(mov_peca)
            else:
                print("\n* Torre de origem vazia.")

        ## Se a torre de origem for 3
        if origem == 3:
            if len(torre3) != 0:
                mov_peca = torre3[-1]
                torre3.remove(mov_peca)
                if destino == 2:
                    torre2.append(mov_peca)
                if destino == 1:
                    torre1.append(mov_peca)
            else:
                print("Torre de origem vazia.")






    else:
        print("\nTorre Inválida!")


def MostrarTorres():
    print("\nTorre 1: ", torre1, '\n', "Torre 2: ", torre2, '\n', "Torre 3: ", torre3)


def aviso_peca():
    print("A peça movida deve ser menor do que a última")


while len(torre3) != discos:
    movimento()
