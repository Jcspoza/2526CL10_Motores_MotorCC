# Taller Programación y Robótica en CMM BML – 2025 - 2026 - CL10 motores CC
# Programa: Control de motor CC con TA6586 - con control de sentido y velocidad
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2026 03
# Licencia : CC BY-NC-SA 4.0
# REf basica https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_motor.html
# 1.0 -> 2.0 comprobar entradas

from machine import Pin, PWM
from utime import sleep

# Informative block - start
p_ucontroler = "Pico _ & W"
p_keyOhw = "TA6586 : BI&FI on GPIO 14 & 15 + MotorCC"
p_project = "Control motor CC by TA6586 velocidad y sentido - con pwm"
p_version = "2.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

BIPIN = 14
FIPIN = 15

BIpwm = PWM(Pin(BIPIN))
FIpwm = PWM(Pin(FIPIN))

# Frecuencia PWM
FIpwm.freq(10000)
BIpwm.freq(10000)

""" Input Truth Table
BI ----- FI ===== BO ===== FO
Low      High     Low      High
High     Low      High     low
High     High     Low      Low
Low      Low      High     High
"""
def Retroceder(vel100=50):
    """vel100 de 0 a 100"""
    
    vel_u16 = int(65535 * vel100 / 100)
    FIpwm.duty_u16(0)
    BIpwm.duty_u16(vel_u16)
    

def Avanzar(vel100=50):
    """vel100 de 0 a 100"""
    
    vel_u16 = int(65535 * vel100 / 100)
    FIpwm.duty_u16(vel_u16)
    BIpwm.duty_u16(0)
    

def Parar():
    """ Para el motor- sin paramentros"""
    
    FIpwm.duty_u16(0)
    BIpwm.duty_u16(0)
    
def LeeVelocidad():
    """ Lee desde teclado la velocidad y la entrega como retorno"""
    
    velocLeido = int(input("Indica la velocidad de giro de 15 a 100 = > "))
    while velocLeido < 15 or velocLeido > 100:
        velocLeido = int(input("Vuelva a indicar la velocidad de giro de 15 a 100 => "))
            
    return velocLeido
    
# Fin funciones
sentido = 'P'

try:
    while True:
        sentido = input("Indica el sentido del giro A avanzar / R retroceder / P parar => ").upper()[0]
        while sentido != "A" and sentido != "R" and sentido != "P":
            sentido = input("Vuelva a indicar el sentido del giro A avanzar / R retroceder / P parar => ").upper()[0]
                    
        if sentido == "A":            
            Avanzar(LeeVelocidad())
        elif sentido == "R":
            Retroceder(LeeVelocidad())
        else:
            Parar()
            
            
except KeyboardInterrupt:
    Parar()
    print("Stop motor - parada de usuario")
