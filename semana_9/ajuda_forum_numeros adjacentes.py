adjacente = False
x = 3
atual = 1
anterior = 2

x = int(input("dígite o número a ser analizado: "))

while not adjacente:    
    
    atual = x % 10
    anterior = ( x // 10 ) % 10

    if atual == anterior:
        adjacente = True
    else:
        x = x//100
        adjacente = False

	
if adjacente:
    print("O número é adjacente")

else:
    print("O número não é adjacente")
