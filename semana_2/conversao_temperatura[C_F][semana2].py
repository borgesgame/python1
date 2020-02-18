#---------------------------------------------------#
# Conversor de Temperatura: Celsius para Fahrenheit #
# Python 3.8.1	25-01-2020 Renan Borgesx	    #
#---------------------------------------------------#

nome = input("DIGITE SEU NOME : ")
print ("Ola", nome, "como vai? ")

tempCelsius  = int(input ("Inisira uma temperatura em Celsius : "))

tempFahrenheit = (tempCelsius * 9) / 5 + 32

print (tempCelsius , " Celsius equivale a ", tempFahrenheit, " Graus Fahrenheit")

