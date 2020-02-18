#---------------------------------------------------------------------#
#	FUNCAO FIZZBUZZ PARTE 3       	 			              #
#	Python 3.8.1 02-02-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def fizzbuzz(num):
    
    num = int(input("Digite um número:")) 

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    elif num % 3 == 0 and not num % 5 == 0:
        print("Fizz")

    elif num % 5 == 0 and not num % 3 == 0:
        print("Buzz")
        
    else:
        print(num)


