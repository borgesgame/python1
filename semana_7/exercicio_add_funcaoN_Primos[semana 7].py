#---------------------------------------------------------------------#
#	FUNCAO N_PRIMO                     		              #
#	Python 3.8.1 05-02-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def n_primos(num):

    while num < 2:
        num = int(input("Oops! Digite um inteiro > ou = 2:"))

    i = 2
    count = num
    qtdPrimo = 0
        

    while count >= 2:        
        primo = True
        
        while i < count and primo:
                        
            if count % i == 0:
                primo = False

            i = i + 1            
            
    
        if primo:        
            qtdPrimo = qtdPrimo + 1
                        
        
        count = count - 1
        i = 2


    return qtdPrimo
    

