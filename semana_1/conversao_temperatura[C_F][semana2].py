#------------------------------------------------------------------------#
#           EXERCICIO DE MATRIZES                                        #
#           Python 3.8.1 08-02-2020 Renan Borgesx                        #
#------------------------------------------------------------------------#

def desenha_matriz(nlinhas,ncolunas):

    matriz = []
    
    for i in range(nlinhas):
        linha = []
        
        for j in range(ncolunas):
            coluna = input("Insira um valor para linha["+ str(i) +"] coluna["+ str(j)+"]: " )
            linha.append(coluna)

        matriz.append(linha)

        print()

    return matriz
  



def matriz():

    i = int(input("Informe quantas linhas: "))
    j = int(input("Informe quantas colunas: "))

    desenha_matriz(i,j)
    
    for ind in range(i):
        print(matriz[ind][:])
