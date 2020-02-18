#---------------------------------------------------------------------#
#       PROGRAMA FINAL CASO COH PIAH                                  #
#       Python 3.8.1 07-02-2020 Renan Borgesx                         #	
#---------------------------------------------------------------------#

import re

def main():

    ass_input = le_assinatura()

    textos = le_textos()

    coh_piah = []
    lista_grau = []
    
    for count in range(len(textos)):
        
        grau = compara_assinatura(
            ass_input,calcula_assinatura(textos[count]))
        
        lista_grau.append(torna_positivo(grau))
        coh_piah.append(count + 1)
        
    print("\n lista_grau:",lista_grau)
    print("\n lista_coh_piah:",coh_piah)    
    
    i = 0
    
    for count in range(len(coh_piah)):
        if sorted(lista_grau)[0] == lista_grau[count]:
            i =  count
            
    
    print("O autor do texto",coh_piah[i],"está infectado com COH-PIAH")
    

    
    
    
    ''' Esta parte compara os textos entre si para achar o grau de similaridade
    for item in textos:
        
        ass_base = calcula_assinatura(item)
        count = 0
        while count < len(textos):
            
            ass_comp = calcula_assinatura(textos[count])            
            if item != textos[count]:
                print("\ncomparando:",ass_base," e ",ass_comp)
                compara_assinatura(ass_base,ass_comp)
                

            count = count + 1'''

def torna_positivo(num):

    if num < 0:
        num = num + (num * 2)
                    
    return num

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
        
    
        
    tamanho_medio_palavras  = soma_caractere / len(palavras)
    relacao_type_token      = n_palavras_diferentes(palavras) / len(palavras)
    razao_hapax_legomana    = n_palavras_unicas(palavras) / len(palavras)
    tamanho_medio_sentencas  = soma_sentencas / len(sentencas) 
    complexibilidade_sentencas = len(frases) / len(sentencas) 
    tamanho_medio_frase = soma_frases / len(frases)

    assinatura = []
    assinatura.append(tamanho_medio_palavras)
    assinatura.append(relacao_type_token)
    assinatura.append(razao_hapax_legomana)
    assinatura.append(tamanho_medio_sentencas)
    assinatura.append(complexibilidade_sentencas)
    assinatura.append(tamanho_medio_frase)

    '''
    print("\n\nTexto original  :",texto[0],)    
    print("\nlista sentencas  :",sentencas,)
    print("\nlista frases     :",frases,) 
    print("\nlista palavras   :",palavras,"\n")
    
    print("TAMANHO MEDIO DE PALAVRAS  - Esse texto contem:",len(palavras),"palavras, total e tamanho medio:",soma_caractere, tamanho_medio_palavras)
    print("RELACAO TYPE TOKEN         - Numero de palavras diferentes:",n_palavras_diferentes(palavras),"relacao type token",relacao_type_token )
    print("RAZAO HAPAX LOGOMANA       - Numero de palavras unicas    :",n_palavras_unicas(palavras),"razao Hapaz Legomana",razao_hapax_legomana )
    print("TAMANHO MEDIO DE SENTENCA  - Esse texto contem:",len(sentencas), "sentencas e a soma e tamanho medio e:",soma_sentencas,tamanho_medio_sentencas)
    print("COMPLEXIBLIDADE DE SENTENCA- Qtd frases:",len(frases),"dividido por qtd sentencas",len(sentencas),"complexibilidade de sentencas",complexibilidade_sentencas)
    print("TAMANHO MEDIO DE FRASE     - Soma de frases",soma_frases,"dividido por qtd frases",len(frases),"tamanho medio de frase",tamanho_medio_frase)
    ''' 

    return assinatura


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

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
    for i in range(len(as_a)):
        #print(dif_ab,"+",as_a[i],"-",as_b[i])
        dif_ab = dif_ab + (as_a[i] - as_b[i])
        #print(dif_ab)
        
    return dif_ab / 6


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass



main()
