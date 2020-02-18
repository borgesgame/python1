#---------------------------------------------------------------------#
#	FUNCAO MAIOR_PRIMO: ENCONTRA O MAIOR NUMERO PRIMO             #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def maior_primo(num):

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


    return maiorPrimo


def test_primo():
    assert maior_primo(100) == 97
    

