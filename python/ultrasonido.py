#!/usr/bin/env python
# -*- coding: utf-8 -*- 
""""
Tomado en gran parte de:
https://electrosome.com/hc-sr04-ultrasonic-sensor-raspberry-pi/

Formula para calcular la distancia

d = V*(t/2) 
V = velocidad del sonido
t = tiempo, que tarda la señal de ir del emisor al obstaculo y volver al receptor
"""


import RPi.GPIO as GPIO                    
import time                                
GPIO.setmode(GPIO.BCM)                     

TRIG = 23                                  #pin 23 como TRIG
ECHO = 24                                  #pin 24 como ECHO
V    = 34300			    			   # Velocidad del sonido 34300cm/s	

print "Medicion de la distancia en curso"

GPIO.setup(TRIG,GPIO.OUT)                  #TRIG como salida
GPIO.setup(ECHO,GPIO.IN)                   #ECHO como entrada

GPIO.output(TRIG, False)                   #TRIG en estado bajo
print "Espere que el sensor se estabilice"
time.sleep(2)                              #Esperar 2 segundos

GPIO.output(TRIG, True)                    #TRIG en estado alto
time.sleep(0.00001)                        #Delay de 0.00001 segundos
GPIO.output(TRIG, False)                   #TRIG en estado bajo

while GPIO.input(ECHO)==0:                 #Comprueba si ECHO está en estado bajo
  pulse_start = time.time()                #Guarda el tiempo transcurrido, mientras esta en estado bajo

while GPIO.input(ECHO)==1:                 #Comprueba si ECHO está en estado alto
  pulse_end = time.time()                  #Guarda el tiempo transcurrido, mientras esta en estado alto

t = pulse_end - pulse_start                #Se obtienen la duración del pulso, calculando la diferencia entre pulse_start  y pulse_end

distancia = t * (V/2)                      #Se multiplica la duración del pulso, por 17150, para obetener la distancia
distancia = round(distancia, 2)            #Se redondea a dos decimales

if distancia > 2 and distancia < 400:      #Comprueba si la distancia está dentro del rango

  print "Distancia: ",distancia,"cm"       #Imprime la distancia 

else:
  print "Fuera de Rango"                   #Imprime fuera de rango

GPIO.cleanup()							   #Limpia los pines	
