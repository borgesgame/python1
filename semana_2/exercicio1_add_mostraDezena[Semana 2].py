#---------------------------------------------------------------------#
#	MOSTRA DADOS CARTAO		 			      #
#	Python 3.8.1 26-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


num = int(input("Digite um número inteiro:"))

num = num % 100
num = num // 10

print ("O dígito das dezenas é", num)
