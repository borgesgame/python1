#---------------------------------------------------------------------#
#	JOGO DO NIM                        		              #
#	Python 3.8.1 02-02-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def computador_escolhe_jogada(n,m):
    num = n
    count = 0
    jogMaxima = True
    
    while count < m:

        count = count + 1

        if (num - 1) % (m + 1) == 0:
            jogMaxima = False
            cpuJogada = count
            
        num = num - 1

    if jogMaxima:
        cpuJogada = m
        
      
    return cpuJogada



def usuario_escolhe_jogada(n,m):

    userJogada = int(input("Quantas peças você vai tirar? "))

    while userJogada <= 0 or userJogada > m:
        print("Oops, jogada inválida! Tente de novo.")
        userJogada = int(input("Quantas peças você vai tirar? "))
    

    print("")
    
    return userJogada


def menu():

    print("")
    print("Bem-Vindo ao JOGO DO NIM! Escolha: ")
    print("")
    
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    escolha = int(input("Escolha: "))
    
    while escolha > 2:
        print("Ooops! Opcao invalida. Tente novamente")
        print("")
        escolha = int(input("Escolha: "))
        
    print("")

    partida(escolha)
    
def partida(x):
    
    if x == 1:
        print("Voce escolheu uma partida isolada")
        i = 1
        
    else:
        print("Você escolheu um campeonato!")
        i = 3
        

    jogar( i )
    
    print("")
    
    
def jogar( i ):

    rodada = 0
    ptCpu = 0
    ptUser = 0
    
    while rodada < i:

        if i == 3:
            if rodada == 0:
                print("")
                print("**** Rodada 1 ****")

            elif rodada == 1:
                print("")
                print("**** Rodada 2 ****")

            else :
                print("")
                print("**** Rodada 3 ****")

        print("")

        
        n = int(input("Quantas peças?: "))
        while n <= 1 :
            print("Oops, valor deve ser maior que 1! Tente de novo.")
            n = int(input("Quantas peças?: "))
            
        m = int(input("Limite de peças por jogada? "))        
        while m <= 0 or m >= n :
            print("Oops, limite deve ser menor que numero de peças! Tente de novo.")
            m = int(input("Limite de peças por jogada? "))

        print("")
        
        if n % (m + 1) == 0:
            print("Você começa!!!")
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada

        else:
            print("Computador começa!")
            print("")
        
        while n > 0 :

            pcGanhou = False

            if n > 0: 
                jogada = computador_escolhe_jogada(n,m)
                n = n - jogada
                
                if n <= 0:
                    pcGanhou = True
                    print(">> O computador tirou [",jogada,"] peças.")
                    
                else:
                    print(">> O computador tirou [",jogada,"] peças.")
                    print("Agora restam [",n,"] peças no tabuleiro.")
                    print("")
            
            if n > 0:
                jogada = usuario_escolhe_jogada(n,m)
                n = n - jogada
                
                if n <= 0:
                    pcGanhou = False
                    
                else:
                    print(">> Você tirou [",jogada,"] peças.")
                    print("Agora restam [",n,"] peças no tabuleiro.")
                    print("")       
       

        if pcGanhou:
            ptCpu = ptCpu + 1
            print("")
            print("Fim do jogo! O computador ganhou!")

        else:
            ptUser = ptUser + 1
            print("")
            print("Fim do jogo! Você ganhou!")


        if i == 1:
            print("")
            print("**** Fim de Partida Isolada ****")
            rodada = 3
            
        else:
            print("Placar: Você",ptUser,"X",ptCpu,"Computador")
            print("")            
            
            if (rodada > 1) and ((ptUser > 2) or (ptCpu > 2)):
                print("**** Fim do Campeonato! ****")
                print("Placar: Você",ptUser,"X",ptCpu,"Computador")
                
                
            rodada = rodada + 1

                
menu()
