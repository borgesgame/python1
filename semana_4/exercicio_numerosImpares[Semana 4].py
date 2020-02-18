#---------------------------------------------------------------------#
#	NUMEROS IMPARES                 		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def main():
        
        num = int(input("Digite o valor de n:"))
        
        count = 0
        count_impar = 0
        play = True
        
        
        while count == 0 or play:

                count = count + 1

                if count % 2 != 0:
                        print(count)
                        count_impar = count_impar + 1

                if count_impar == num:
                        play = False
                        

main()
