x = int(input("dígite o número a ser analizado: "))

atual = 1
anterior = 2
adjacente = False

while atual != anterior and not adjacente:
    
    atual = x%10
    anterior = (x//10)%10

    if atual != anterior:
        adjacente = False
        ''' acrescentado verificacao da 3 casa decimal'''
        x = x//100
        atual = x
        
    else:
        adjacente = True

    if atual == anterior:
            adjacente = True
    

if adjacente == True:
	print("O número é adjacente")
else:
	print("O número não é adjacente")
