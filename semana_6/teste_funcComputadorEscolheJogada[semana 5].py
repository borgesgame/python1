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
            jogada = count
            
        num = num - 1

    if jogMaxima:
        jogada = m
        
      
    return jogada



