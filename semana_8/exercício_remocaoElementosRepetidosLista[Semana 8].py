#---------------------------------------------------------------------#
#       REMOVENDO ELEMENTOS REPETIDOS DE UMA LISTA                    #
#       Python 3.8.1 05-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def remove_repetidos(lista):    
            
    for count in range(len(lista)):
        
        x = len(lista) - 1
        while x > count:
        
            if lista[count] == lista[x]:    
                del lista[x]

            x = x - 1

    
    #lista.sort() modifica a lista permanentemente

    return sorted(lista)
