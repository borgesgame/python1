#---------------------------------------------------------------------#
#       CALCULO FATORIAL C/ WHILE                                     #
#       Python 3.8.1 28-01-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

def main():
    n = 0

    while n  >= 0:
        n = int(input("Informe um numero a ser fatorado: "))
        if n >= 0:
            fatorial( n )

def fatorial( n ):
    count = 1
    calcFatorial = 1

    while count < n :
        count +=1
        calcFatorial = calcFatorial * count

    print("O fatorial de (",n,") é: ",calcFatorial, "\n")
		
main()
