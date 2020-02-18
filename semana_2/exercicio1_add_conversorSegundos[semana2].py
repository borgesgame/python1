#---------------------------------------------------#
# Conversor de Segundos: Dias, Horas, Minutos       #
# Python 3.8.1	25-01-2020 Renan Borgesx	    #
#---------------------------------------------------#

totalSeg = int(input ("Por favor, entre com o número de segundos que deseja converter:"))

dias = int(totalSeg // 86400)

horas = int((totalSeg % 86400) / 3600)

minutos = int((totalSeg % 3600) / 60)

segundos = totalSeg % 60

print (dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos." )

