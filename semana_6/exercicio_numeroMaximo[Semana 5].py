#---------------------------------------------------------------------#
#	NUMERO MAXIMO                          		              #
#	Python 3.8.1 29-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def main():
    n1 = int(input("Digite primeiro numero inteiro: "))
    n2 = int(input("Digite segundo numero inteiro: "))

    numeroMaximo(n1,n2)
    
    
    

def numeroMaximo(x,y):

    if x > y:
        maximo = x
        minimo = y

    else:
        maximo = y
        minimo = x

    print("maximo (",maximo,",",minimo,")")


main()
    
