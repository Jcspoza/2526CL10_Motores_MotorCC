# Taller Programación y Robótica en CMM BML – 2025 - 2026 - CL10 motores CC
# Programa: Control de motor CC con TA6586 - basico
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2026 03
# Licencia : CC BY-NC-SA 4.0
# REf basica https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_motor.html

from machine import Pin
from utime import sleep

# Informative block - start
p_ucontroler = "Pico _ & W"
p_keyOhw = "TA6586 : BI&FI on GPIO 14 & 15 + MotorCC"
p_project = "Control motor CC by TA6586 - NO pwm"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

BIPIN = 14
FIPIN = 15

BackwardInput = Pin(BIPIN, machine.Pin.OUT)
ForwardInput = Pin(FIPIN, machine.Pin.OUT)
""" Input Truth Table
BI ----- FI ===== BO ===== FO
Low      High     Low      High
High     Low      High     low
High     High     Low      Low
Low      Low      High     High
"""
def clockwise():
    BackwardInput.high()
    ForwardInput.low()

def anticlockwise():
    BackwardInput.low()
    ForwardInput.high()

def stopMotor():
    BackwardInput.low()
    ForwardInput.low()
try:
    while True:
        clockwise()
        print('clockwise 2 seg')
        sleep(2)
        stopMotor()
        print('Stop 5 seg')
        sleep(5)
        anticlockwise()
        print('anti-clockwise 2 seg')
        sleep(2)
        stopMotor()
        print('Stop 5 seg')
        sleep(5)
except KeyboardInterrupt:
    stopMotor()
    print("Stop motor - parada de usuario")
