#---------------------------------------------------------------------#
#	JOGO DO NIM                        		              #
#	Python 3.8.1 rev.20-02-2020 Renan Borgesx                     #
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

        userJogada = int(input(">> Quantas peças você vai tirar? "))

        while userJogada <= 0 or userJogada > m:
            print("Oops, jogada inválida! Tente de novo.")
            userJogada = int(input(">> Quantas peças você vai tirar?"))
                
        return userJogada


def menu():

        print("\n Bem-Vindo ao JOGO DO NIM! Escolha: \n") # Menu de escolha partida isolada / campeonado
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        escolha = int(input("Escolha: "))
        
        while escolha > 2:
            print("Ooops! Opcao invalida. Tente novamente")
            print("")
            escolha = int(input("Escolha: \n"))
    
        if escolha == 1:
            print("Voce escolheu uma partida isolada")
            i = 1
            
        else:
            print("Você escolheu um campeonato!\n")
            i = 3
            
        partida(i) 
    
    
def partida(i):

        rodada = 0
        ptCpu = 0
        ptUser = 0
        
        while rodada < i: # Bloco de processamento de rodadas [isolada=1 rodada, campeonato=3 rodadas]
            if i == 3:
                if rodada == 0:
                    print("\n**** Rodada 1 ****\n")

                elif rodada == 1:
                    print("\n**** Rodada 2 ****\n")

                else :
                    print("\n**** Rodada 3 ****\n")


            
            n = int(input("Quantas peças?: ")) # Escolha de quantidade de peças do jogo.
            while n <= 1 :
                print("Oops, valor deve ser maior que 1! Tente de novo.")
                n = int(input("Quantas peças?: "))
                
            m = int(input("Limite de peças por jogada? ")) # Escolha de limite de peças do jogo.
            while m <= 0 or m >= n :
                print("Oops, limite deve ser menor que numero de peças! Tente de novo.")
                m = int(input("Limite de peças por jogada? "))


            #Escolha de quem começa o jogando.
            if n % (m + 1) == 0:
                print("\nVocê começa!!!\n")
                jogada = usuario_escolhe_jogada(n,m)
                n = n - jogada
                                  
                print("Você tirou [",jogada,"] peças.")
                print("Agora restam [",n,"] peças no tabuleiro.\n")
                
            else:
                print("Computador começa!\n")
            


            while n > 0 : # Bloco de processamento das jogadas de cada rodada

                pcGanhou = False
                if n > 0: # Condicional controle de jogadas computador                 
                    jogada = computador_escolhe_jogada(n,m)
                    n = n - jogada
                    
                    if n <= 0: 
                        pcGanhou = True
                        print(">> O computador tirou [",jogada,"] peças.")
                        
                    else:
                        print(">> O computador tirou [",jogada,"] peças.")
                        print("Agora restam [",n,"] peças no tabuleiro.\n")
                

                if n > 0: # Condicional controle de jogadas usuario                    
                    jogada = usuario_escolhe_jogada(n,m)
                    n = n - jogada
                    
                    if n <= 0:
                        pcGanhou = False
                        
                    else:
                        print("Você tirou [",jogada,"] peças.")
                        print("Agora restam [",n,"] peças no tabuleiro.\n")       
           

            if pcGanhou:
                ptCpu = ptCpu + 1
                print("\nFim do jogo! O computador ganhou!")

            else:
                ptUser = ptUser + 1
                print("\nFim do jogo! Você ganhou!")


            if i == 1:
                print("\n**** Fim de Partida Isolada ****")
                rodada = 3
                
            else:
                print("Placar: Você",ptUser,"X",ptCpu,"Computador\n")            
                
                if (rodada > 1) and ((ptUser > 2) or (ptCpu > 2)):
                    print("**** Fim do Campeonato! ****")
                    print("Placar: Você",ptUser,"X",ptCpu,"Computador")
                                        
                rodada = rodada + 1

                
menu()
