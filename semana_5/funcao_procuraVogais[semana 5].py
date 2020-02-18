#---------------------------------------------------------------------#
#	FUNCAO VOGAL: PROCURA VOGAIS           		              #
#	Python 3.8.1 02-02-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def vogal(char):

    teste = False
    
    if char == 'a' or char == 'A':
        teste = True
    elif char == 'e' or char == 'E':
        teste = True
    elif char == 'i' or char == 'I':
        teste = True
    elif char == 'o' or char == 'O':
        teste = True
    elif char == 'u' or char == 'U':
        teste = True
    else:
        teste = False
        
       
    return teste


    

