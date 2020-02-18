#---------------------------------------------------------------------#
#	MOSTRA NUMEROS PRIMOS               		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def main():

    num = int(input("Digite um número inteiro:"))
    count = 2
    primo = True

    while count < num and primo:
                
        if num % count == 0:
            primo = False            
           
        count = count + 1
                

    if primo:    
        print ("primo")
        
    else:
        print ("não primo")

    
main()
