#---------------------------------------------------------------------#
#	FUNCAO FIZZBUZZ        	 			              #
#	Python 3.8.1 02-02-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def fizzbuzz(num):
    
    if num % 3 == 0 and num % 5 == 0:
        display = "FizzBuzz"

    elif num % 3 == 0 and not num % 5 == 0:
        display = "Fizz"

    elif num % 5 == 0 and not num % 3 == 0:
        display = "Buzz"
        
    else:
        display = num

    return display
