#---------------------------------------------------------------------#
#	FUNCAO SOMA HIPOTENUSAS               		              #
#	Python 3.8.1 05-02-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def soma_hipotenusas(n):

    soma = 0
    count = 1
    while count <= n:

        if é_hipotenusa(count):
            soma = soma + count

        count = count + 1

    return soma


  
def é_hipotenusa(num):

    check = False
    a = 1
    b = 1


    while not check and (a**2 + b**2) < num**2:
        check = False
        
        while not check and (a**2 + b**2) <= num**2:
            
            if a**2 + b**2 == num**2:
                check = True

            b = b + 1

        a = a + 1
        b = 1

    return check
    




    
    

