# Taller Programación y Robótica en CMM BML – 2025 - 2026 - CL10 motores CC
# Programa: Control de motor CC con TA6586 + Rotary encoder
# - con control de velocidad
# Hardware platform: Pico _ & W / funciona igual sin cambios
# Librerias : Ninguna
# Ref librerias: 
# Fecha JCSP 2026 03
# Licencia : CC BY-NC-SA 4.0
# REf basica https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_motor.html
# 1.0 

from machine import Pin, PWM
from utime import sleep, sleep_ms
from rotary_irq_rp2 import RotaryIRQ

# Informative block - start
p_ucontroler = "Pico _ & W"
p_keyOhw = "TA6586 : BI&FI on GPIO 14 & 15 + MotorCC + R. encioder 16&17"
p_project = "Control motor CC by TA6586 velocidad por R. encoder - con pwm"
p_version = "1.0"
print(f"Microcontroler: {p_ucontroler} - Key other HW : {p_keyOhw}")
print(f"Program: {p_project} - Version: {p_version}")
# Informative block - end

# 0- los 2 pines del Rotary Encoder, si el incremento es decremento -> invertir
TRA = 16
TRB = 19

#1- Creacion  del objeto
r = RotaryIRQ(
    pin_num_clk=17,
    pin_num_dt=16,
    min_val=15,
    max_val=100,
    reverse=False,
    incr=5,
    range_mode=RotaryIRQ.RANGE_WRAP,
    # pull_up=True,
    half_step=False,
    )


# Motor CC
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
    """ Lee desde R. Encoder la velocidad y la entrega como retorno"""
    
    velocidad_RE = r.value()
   
    return velocidad_RE
       
# Fin funciones

try:
    while True:
        velocidad_act = LeeVelocidad()
        print(f"Velocidad de giro de 10 a 100. Actual = {velocidad_act} %", end= '\r' )
        Avanzar(velocidad_act)
        sleep_ms(500)        
            
            
except KeyboardInterrupt:
    Parar()
    print("Stop motor - parada de usuario")
