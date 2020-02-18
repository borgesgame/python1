#---------------------------------------------------------------------#
#	NUMERO BINOMIAL                 		              #
#	Python 3.8.1 29-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def NumeroBinomial():
    count = 0

    while count < 3:
        
        num = int(input("Digite o valor de n:"))
        print ("Fatorial de", num,"é:", fatorial( num ))
        count = count + 1      




def fatorial( n ):
    
    count = 1
    calcFatorial = 1
    
    while count < n :

        count +=1
        calcFatorial = calcFatorial * count


    return calcFatorial
    
	
NumeroBinomial()
