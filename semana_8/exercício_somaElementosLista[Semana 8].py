#---------------------------------------------------------------------#
#       SOMA ELEMENTOS DE UMA LISTA                                   #
#       Python 3.8.1 05-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def soma_elementos(lista):    

    soma = 0
    
    for count in range(len(lista)):
        
        soma = soma + lista[count]

    
    return soma

