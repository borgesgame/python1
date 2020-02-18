numero = int(input("dígite o número a ser analizado: "))
adjacente = False

timer =  len(str(numero))
cont = 0

while cont < timer and not adjacente:
    valor = numero % 10
    numero2 = numero // 10
    valorAdj = numero2 % 10

    cont += 1
    if valor == valorAdj:
        adjacente = True
       
    else:
        adjacente = False
        numero //= 10
    

if adjacente:
	print("há um número adjacente")
else:
	print("Não há um numero adjacente")
