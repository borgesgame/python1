#---------------------------------------------------------------------#
#	FUNCAO MAXIMO DE TRES: RETORNA NUMERO MAXIMO                  #
#	Python 3.8.1 29-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def maximo(x,y,z):

    if x > y and x > z :
        maior = x

    elif y > x and y > z :
        maior = y
        
    else:
        maior = z
        

    return maior



    
