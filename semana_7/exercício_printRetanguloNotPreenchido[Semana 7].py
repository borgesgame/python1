#---------------------------------------------------------------------#
#       DESENHA RETANGULO NOT PREENCHIDO                              #
#       Python 3.8.1 05-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def main():

    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))		

    a = 1

    while a <= altura:
        
        l = 1                
        while l <= largura:
            
            if a == 1 or a == altura:
                print("#", end='')

            else:
                if l == 1 or l == largura:
                    print("#", end='')
                else:
                    print(" ", end='')                

            l = l + 1
                

        print()        
        a = a + 1
        

main()
