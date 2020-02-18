#---------------------------------------------------------------------#
#	MAIOR NUMERO PRIMO               		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#



def main():

    n = int(input("Digite um número inteiro maior ou igual a 2:"))

    if n < 2:
        while n < 2:
            n = int(input("Digite um número inteiro maior ou igual a 2:"))
        
    ePrimo(n)        
  


def ePrimo(num):

    i = 2
    count = num
    primo = False
    maiorPrimo = num
    

    while count > 2 and not primo:        
        primo = True
        
        while i < count and primo:
                        
            if count % i == 0:
                primo = False

            i = i + 1            
            
    
            if primo:        
                maiorPrimo = count
                        
            else:
                count = count - 1
                i = 2


    print("maior_primo(",maiorPrimo,")")


    
main()
