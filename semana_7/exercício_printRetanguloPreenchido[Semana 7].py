#---------------------------------------------------------------------#
#       DESENHA RETANGULO PREENCHIDO                                  #
#       Python 3.8.1 05-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def main():

    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))		

    a = 0

    while a < altura:
        
        l = 0
        while l < largura:
            print("#", end='') 
            l = l + 1

        print()
        l = 0
        a = a + 1
        

main()
