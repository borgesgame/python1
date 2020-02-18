#---------------------------------------------------------------------#
#	DIGITO ADJACENTE                		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def main():
        
        num = input("Digite um número inteiro:")
        
        count = 0
        noRepete = True
        
        i = int(len(num)) 
        num = int(num)
        
        divisorResto = 10
        divisor = 1


        while num != 0 and count < i and noRepete :                

                n1 = num % divisorResto // divisor                

                divisorResto = divisorResto * 10
                divisor = divisor * 10

                n2 = num % divisorResto // divisor
                

                if n1 == n2:
                        noRepete = False                       
                        
                else:                
                        count = count + 1
	
        if noRepete:
                print("não")

        else:
                print("sim")
	
main()
