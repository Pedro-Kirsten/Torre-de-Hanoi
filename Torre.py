print("  ■                      ■\n ■■■   TORRE DE HANÓI   ■■■\n■■■■■                  ■■■■■   ")

torre = [[], [], []] #Inicializa as torres

discos = int(input("\nQuantidade de discos (3 - 8): ")) #Recebe a quantidade e distribui os discos
for i in range(0, discos):
   torre[0].append(discos - i)




def mostrarTorres():    #Exibir o conteúdo das torres
   print("\n Torre 1: ", torre[0], '\n', "Torre 2: ", torre[1], '\n', "Torre 3: ", torre[2])

def movimento():
   origem = int(input("\nTorre de origem: ")) - 1
   destino = int(input("\nTorre de destino: ")) - 1
   if origem >= 0 and origem <= 2 and destino >= 0 and destino <= 2:  #Verifica se a origem e destino são validos
       if len(torre[origem]) != 0:                                    #Verifica se a torre de origem não está vazia
           if len(torre[destino]) == 0 or torre[origem][-1] < torre[destino][-1]: #Verifica se o movimento é válido
               torre[destino].append(torre[origem][-1])
               torre[origem].remove(torre[origem][-1])
               mostrarTorres()
           else: ("\n*** Movimento Inválido ***")
       else: print("\n*** Torre de Origem Vazia ***")
   else: print("\n*** Torre Inválida ***")




if discos > 2 and discos < 9:       #Verifica a quantidade de discos
   mostrarTorres()
   while len(torre[2]) != discos:  #Repetição
       movimento()
   print("\nSucesso!")
else: print("*** Escolha entre 3 e 8 discos ***")




