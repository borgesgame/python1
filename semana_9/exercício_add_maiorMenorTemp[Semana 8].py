#---------------------------------------------------------------------#
#       MAIOR e MENOR TEMPERATURA DE UMA LISTA                        #
#       Python 3.8.1 06-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def maior_menor_temp(lista):

    diaMaior = 0
    diaMenor = 0
            
    for count in range(len(lista)):

        if lista[count] == sorted(lista)[-1]:
            diaMaior = count + 1
            
        if lista[count] == sorted(lista)[0]:
            diaMenor = count + 1
            
    return print("Maior Temperatura",sorted(lista)[-1],"C no dia",diaMaior, 
                 "\nMenor Temperatura",sorted(lista)[0],"C no dia",diaMenor)
