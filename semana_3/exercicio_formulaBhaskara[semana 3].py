#---------------------------------------------------------------------#
#	CALCULO RAIZES QUADRATICAS	 			      #
#	Python 3.8.1 26-01-2020 Renan Borgesx	                      #
#---------------------------------------------------------------------#


def main():
    import math
    print("PROGRAMA - CALCULO DE ESQUACAO DE SEGUNDO GRAU")
    print()

    a = int(input("Insira o valor de a:"))
    b = int(input("Insira o valor de b:"))
    c = int(input("Insira o valor de c:"))
    print()

    delta = b**2 - 4*a*c
    
    if delta >= 0:
        if delta > 0:
            raiz_1 = (-b + math.sqrt(delta)) / (2*a)
            raiz_2 = (-b - math.sqrt(delta)) / (2*a)
            
            if raiz_1 < raiz_2:
                print("as raízes da equação são",raiz_1,"e",raiz_2)
            else:
                print("as raízes da equação são",raiz_2,"e",raiz_1)
        
        
        if delta == 0:
            raiz_1 = -b / (2*a)
            print("a raiz desta equação é",raiz_1)

    else:        
        print("esta equação não possui raízes reais")        

main()
