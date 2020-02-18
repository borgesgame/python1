#---------------------------------------------------------------------#
#	CALCULO FATORIAL                		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def main():

    n = int(input("Digite o valor de n:"))
    count = 1
    calcFatorial = 1
    
    while count < n :

        count +=1
        calcFatorial = calcFatorial * count

    print(calcFatorial)
    
main()
