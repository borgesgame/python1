#---------------------------------------------------------------------#
#	DISTANCIA ENTRE DOIS PONTOS  	        	              #
#	Python 3.8.1 27-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def main():
    import math
    x1 = int(input("Digite primeiro número:"))
    y1 = int(input("Digite segundo número:"))
    x2 = int(input("Digite terceiro número:"))
    y2 = int(input("Digite quarto número:"))

    distancia = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

    if distancia >=10:
        print("longe")

    else:
        print("perto")


main()
