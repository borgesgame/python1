#---------------------------------------------------------------------#
#	CALCULO SOMA DE DIGITOS                		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def main():
        
        num = input("Digite um número inteiro:")
        
        count = 0
        soma = 0
        
        i = int(len(num)) 
        num = int(num)
        
        divisorResto = 10
        divisor = 1


        while count < i:                

                result = num % divisorResto // divisor
                soma = soma + result

                divisorResto = divisorResto * 10
                divisor = divisor * 10
                
                count = count + 1
	
        print(soma)
	
main()
