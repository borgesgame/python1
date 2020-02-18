#---------------------------------------------------------------------#
#       LISTA INVERSA                                                 #
#       Python 3.8.1 06-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def main():    

    lista = []
    item = ""
        
    while item != '0':
        item = input("Insira um numero inteiro[0 para finalizar]: ")
        lista.append(item)
    
    
    for i in range(2,len(lista)+1):
        print(lista[-i])


main()
