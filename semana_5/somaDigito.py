#---------------------------------------------------------------------#
#	CALCULO SOMA DE DIGITOS                		              #
#	Python 3.8.1 28-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#

def main():
        n = input("Digite um numero inteiro: ")
        somaDigitos(n)


def somaDigitos(num):
               
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
        
        

def test_somaZero():
        assert somaDigitos(00) == 0

main()
	

