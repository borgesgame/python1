#---------------------------------------------------------------------#
#	VERIFICANDO ORDENAÇAO DOS NUMEROS		              #
#	Python 3.8.1 26-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def main():
    num1 = int(input("Digite primeiro número:"))
    num2 = int(input("Digite segundo número:"))
    num3 = int(input("Digite terceiro número:"))

    if num1 < num2 and num2 < num3:
        print("crescente")

    else:
        print("não está em ordem crescente")


main()
