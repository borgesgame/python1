#---------------------------------------------------#
# Conversor de Temperatura: Fahrenheit para Celsius #
# Python 3.8.1	25-01-2020 Renan Borgesx			#
#---------------------------------------------------#

nome = input("DIGITE SEU NOME : ")
print ("Ola", nome, "como vai? ")

tempFahrenheit = int(input ("Inisira uma temperatura em Fahrenheit : "))

tempCelsius = (( tempFahrenheit - 32) * 5) / 9

print (tempFahrenheit, " Fahrenheit equivale a ", int(tempCelsius), " Graus Celsius")

