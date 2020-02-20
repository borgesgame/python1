#---------------------------------------------------------------------#
#       PROGRAMA FINAL CASO COH PIAH                                  #
#       Python 3.8.1 07-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

import re

def main():

    print("\nBem-vindo ao detector automático de COH-PIAH.\n")

    escolha = -1

    while escolha != 0:
        print("\nEsolha uma opção [1] [2]\n")
        print("[1] Informe uma assinatura e textos para achar copiadores :)")
        print("[2] Gere a assinatura contendo os tracos linguisticos de um texto")
        print("[3] Compare varios textos para achar similaridades ")
        escolha = int(input("escolha uma opção: "))

        if escolha == 1:# OPCAO 1 - Informe uma assinatura e textos para achar copiadores 
            ass_input = le_assinatura()
            textos = le_textos()
            avalia_textos(textos, ass_input)
            print("\n\n\n")
            
        elif escolha == 2:
            texto = input("\nDigite o texto (aperte enter para enviar):")
            ass_texto = calcula_assinatura(texto)
            print("\nAssinatura calculada:\n")

            print("Tamanho medio de palavra      : ",ass_texto[0])
            print("Relação Type-Token            : ",ass_texto[1])
            print("Razão Hapax Legomana          : ",ass_texto[2])
            print("Tamanho médio de sentença     : ",ass_texto[3])
            print("Complexidade média da sentença: ",ass_texto[4])
            print("Tamanho medio de frase        : ",ass_texto[5])

            print("\n\n\n")

        elif escolha ==3:
            textos = le_textos()
            compara_entresi(textos)
            
    print("Obrigado por utilizar, ate mais :-)!!")
    
def torna_positivo(num):

    if num < 0:
        num = num * -1
                    
    return num

def compara_entresi(textos):
    '''Esta parte compara os textos entre si para achar o grau de similaridade'''
    texto1 = 0
    print(" ________________________________________________")
    print("|        COMPARANDO        |     RESULTADOS      |")
    for item in textos:
        texto1 += 1
        texto2 = 0
        
        ass_base = calcula_assinatura(item)
        count = 0
        while count < len(textos):
            texto2 += 1
            
            ass_comp = calcula_assinatura(textos[count])            
            if item != textos[count]:
                print("|  Texto(",texto1,") e Texto(",texto2,") | ",compara_assinatura(ass_base,ass_comp))
                
                
            count = count + 1
    print("--------------------------------------------------")

    
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("\nBem-vindo ao detector automático de COH-PIAH.\n")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    ''' Observacoes: Sentenca consiste em um texto sem . ! ?'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''

    dif_ab = 0
    for i in range(6):
        ''' Calculo da soma da diferença entre valores da assinatura de a e b '''
        dif_ab = dif_ab + torna_positivo(as_a[i] - as_b[i])
       
        
    return dif_ab / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''    
    sentencas = separa_sentencas(texto)
 
    count = 1
    frases = separa_frases(sentencas[0])
    while count < len(sentencas):
        frases = frases + separa_frases(sentencas[count])
        count = count + 1

    count = 1
    palavras = separa_palavras(frases[0])
    while count < len(frases):
        palavras = palavras + separa_palavras(frases[count])
        count = count + 1
    
    soma_caractere = 0
    for item in palavras:
        soma_caractere = soma_caractere + len(item)

    soma_sentencas = 0
    for item in sentencas:
        soma_sentencas = soma_sentencas + len(item)

    soma_frases = 0
    for item in frases:
        soma_frases = soma_frases + len(item)        
        
    
        
    tamanho_medio_palavras      = soma_caractere / len(palavras)
    relacao_type_token          = n_palavras_diferentes(palavras) / len(palavras)
    razao_hapax_legomana        = n_palavras_unicas(palavras) / len(palavras)
    tamanho_medio_sentencas     = soma_sentencas / len(sentencas) 
    complexibilidade_sentencas  = len(frases) / len(sentencas) 
    tamanho_medio_frase         = soma_frases / len(frases)

    return [tamanho_medio_palavras, relacao_type_token, razao_hapax_legomana,
            tamanho_medio_sentencas, complexibilidade_sentencas, tamanho_medio_frase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver
    o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    coh_piah = []
    lista_grau = []
    #contador = re.split(r'[.!?]+', textos)
    
    for count in range(len(textos)):
        
        grau = compara_assinatura(
            ass_cp,calcula_assinatura(textos[count]))
        
        lista_grau.append(torna_positivo(grau))
        coh_piah.append(count + 1)
          
    
    i = 0    
    for count in range(len(coh_piah)):
        if sorted(lista_grau)[0] == lista_grau[count]:
            i =  count
            
    print("\n"+ str(len(textos)) +"textos verificados:\n")
    print("O autor do texto",coh_piah[i],"está infectado com COH-PIAH")

    return coh_piah[i]


main()
