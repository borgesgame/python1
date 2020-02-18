#---------------------------------------------------------------------#
#       LISTA INVERSA                                                 #
#       Python 3.8.1 05-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def main():

    lista = []
    item = ""
        
    while item != '0':
        item = input("Insira um numero [0 para finalizar]: ")
        lista.append(item)
    
    i  = len(lista)
    count = 0

    print("\nLista Informada: ", end='')
    while count < len(lista) - 1 :
        
        print(lista[count], end=' ')

        count = count + 1


    i  = len(lista)
    count = 0
     
    print("\nLista Inversa: ", end='')
    while count < len(lista) - 1:
       
        i = i - 1
        
        print(lista[i - 1], end=' ')

        count = count + 1       

    
main()
