#---------------------------------------------------------------------#
#	FIZZBUZZ PARTE 3       	 			              #
#	Python 3.8.1 26-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def main():
    num = int(input("Digite um número:"))

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    else:
        print(num)

main()
