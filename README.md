# 2526CL10_Motores_MotorCC

Panoiramica de Motores en robótica + Controlar Motores de Corriente Cntinua

Indice evolutivo del las clases del taller + libros y webs de referencia:

[GitHub - Jcspoza/2526_PyR_Index: Curso Programación y Robotica 2025 2026 - CMM BML](https://github.com/Jcspoza/2526_PyR_Index)

## 

---

## Proyecto completo-> en inicio de pruebas : sensor humedad suelo + bomba agua (motor)

Esta lección forma parte del los aprendizajes necesarios para controlar cargas analógicas de cierta potencia como un motor

## Clase10 - Indice

- Panorama de motores en Robótica

- Introducción a los motores de Corriente continua

- * Lista de materiales
  
  * Links a Tutoriales  e informacion
  - Librerías importantes - No necesarias

- Control de motores de CC en robotica
  
  - M#0- Control por PWM transistor BJC npn ( visto en 2526 CL9) : **Velocidad / No Sentido de giro**
  - M#1- Control con integrado TA6586 : 
    - Programa 1.0 : No velocidad / Si sentido de giro
    - Programa 2.0 con PWM : SI velocidad / Si sentido de giro
  - M#2- Control con integrado TA6586 + Display SH1106 y Rotary encoder
    - programa 1.0 : SI velocidad con R. Encoder + giro con pulsador
    - programa 2.0 : SI velocidad con R. Encoder + giro con pulsador + display

- Tabla resumen de programas

- TO DO y Notas

## Panorama de motores en Robótica

Hay 3 grades grupos de motores en robotica:

1. **Motores servo** : se controla el ángulo de giro en un arco de 0º  a 180º
   
   <u>Uso  típico</u> : brazos robóticos, algun mecanismo que solo requiera giros de 0 a 180, como cerraduras 

2. **Motores paso a paso** 
   
   <u>Uso típico</u> : impresoras 3D para posicionar la cabeza impresora, u otras maquinas donde el movimiento circular se cambia a lineal, de forma que se pueda controlar la posicion con precisión

3. **Motores de corriente continua**
   
   <u>Uso típico</u> : ruedas de vehículos robóticos, como coches teledirigidos y drones. Tienen 2 sentidos de giro ; horario y anti-horario, asi como control de velocidad 

Para el **proyecto de riego automático** necesitamos controlar un motor de CC, asi que nos centraremos en como controlarlo tanto en sentido de giro como en velocidad.

## Introducción a los motores de Corriente continua en robótica

### Entender como funciona un motor CC ( con rozamiento)

Se puede empezar con el **tutorial** de Sunfounder

[DC Motor &mdash; SunFounder Pico 2 W Starter Kit for Raspberry Pi Pico 2 W documentation](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_dc_motor.html)

o esta simulación

[**DC Motor** - Magnet Academy - MagLab](https://www.google.com/url?client=internal-element-cse&cx=004099242236933193842:9shljmjve7a&q=https://nationalmaglab.org/magnet-academy/watch-play/interactive-tutorials/dc-motor/&sa=U&ved=2ahUKEwj-xPqb7KaTAxVxbKQEHRdWAUMQFnoECAUQAQ&usg=AOvVaw1thIX6Ns0QQQgaSmAViyBW&fexp=121574859,121574858,73152292,73152290)

### Controlar motores CC en robotica

Después recomiendo la serie de tutoriales de la web [Learning micropython](https://dmccreary.github.io/learning-micropython/) , **aunque la serie esta incompleta!!!**

    [Motor Introduction - Learning MicroPython](https://dmccreary.github.io/learning-micropython/motors/01-intro/)

porque siguen la lógica de aprendizaje que creo la mejor.

Es decir, **lo ideal es hacer en orden los siguientes montajes**

1. (M#0) Controlar motor CC con **1 transistor sin / con PWM**

2. Controlar motor CC con un **puente en H de transistores**  ( no se suele hacer)

3. Controlar motorCC con un **chip** de puente en H, o similar
   
   * Chip L293D ( no en kit SF)
   * Chip L298N (no en kit SF)
   * Chip TB6612FNG (no en kit SF - usa MOSFET)
   * chip DRV8833 ( no en kit SF - usa MOSFET) : es el mas recomendado
   * **(M#1) chip TA6586 - en kit SF == > haremos este porque esta en el kit - montaje básico**
   * ....
     4* (M#2) Chip TA6586 + control por Rotary encoder + Display - PENDIENTE

### Escoger el chip de control de motores (en general)

Otra opcion, es escoger el chip de control y a partir de ahí, buscar tutoriales para ese chip:

![](./doc/drivers_motores_DC_comparativa.png)

### Escoger el chip de control de motores - para nuestro proyecto de riego

**Vamos a usar el chip TA6586** o un transistor S8050 porque 

- Vienen con el kit

- Solo necesitamos 1 motor para la bomba o varios en paralelo

- Tanto el chip como el transistor pueden manejar 1 solo motor, o **varios motores en paralelo**
  
  - **no se necesita cambiar el sentido**
  
  - quizá si la velocidad
  
  - Hay algun [riesgo de poner motores en paralelo : ver info completa dada por IA](./doc/2motores_paralelo_TA6586.pdf)

Asi que vamos a estudiar como controlar un motor con el chip TA6586 y con transistor S8050

## Materiales y links a información

### Materiales

| Material                                                                                                                   | Descripcion                                                                                                                                                      | Kit SF                       | Montaje   |
| -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | --------- |
| [Protoboard 700](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_breadboard.html)            | Placa para prototipos ver apartado [Uso de la protoboard](https://github.com/Jcspoza/2526CL1_R_CircElect0#uso-de-la-protoboard). Mejor usar la protoboard de 700 | SI                           | Todos     |
| [Cables dupond M-M](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_wire.html)               | Sirven para hacer conexiones en protoboard                                                                                                                       | SI                           | Todos     |
| Pico _, 2, W, 2W                                                                                                           | Vale cualquiera de los 4 modelos de Pico                                                                                                                         | SI                           | Todos     |
| [Transistor BJC NPN S8050](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/component/component_transistor.html) |                                                                                                                                                                  | SI                           | Mon#0     |
| Resistencias 1k y 10k                                                                                                      | para polarización de transistor en Emisor común                                                                                                                  | SI                           | Mon#0     |
| Diodo 1N4007                                                                                                               | Diodo fly-back evita poicos cuando se corta tensi2motores_paralelo_TA6586.pdfon en bobinas                                                                       | SI                           | Mon#0     |
| Motor de 5 volt nominales                                                                                                  |                                                                                                                                                                  | SI                           | Todos     |
| Alimentación del motor entre 5 y 9 volt                                                                                    | Lo mas sencillo es un apila de 9 volt , también vale un cargador viejo de entre 5 y 9 volt                                                                       | NO                           | Todos     |
| [TA6586](https://docs.sunfounder.com/projects/kepler-kit/en/latest/component/component_ta6585.html)                        | Chip controlador de motor CC ver comparativa de drivers de motores                                                                                               | SI                           | Mon#1, #2 |
| Display SH1106 + R. encoder  pulsadores                                                                                    |                                                                                                                                                                  | No , pero comprado por todos | Mon#2     |

### Links a informacion

| Tema | Link                                                                                                                      |
| ---- | ------------------------------------------------------------------------------------------------------------------------- |
| PWM  | [kit kepler Sunfounder 2.3 Fading LED](https://docs.sunfounder.com/projects/pico-2w-kit/en/latest/pyproject/py_fade.html) |
|      |                                                                                                                           |

### Librerías importantes - No son necesarias en CL10

.

## Control de motores de CC en robotica

### 1. Montaje M#0- Control por PWM y transistor BJC npn (visto en 2526 CL9)- Control de velocidad / NO sentido de giro

En la clase 9 de 2026, ya vimos un primer caso de control de motores en CC

- 4toMontaje de CL9: Controlar MOTOR a 9 volt desde 3,3 volt con Transistor BJC (con PICO) por PWM

Copio toda la info por facilidad

#### Explicación control por PWM y NPN

#### Montaje

![](./doc/SalidaPWM_motor_bb.png)

#### Porque hay que usar un diodo en paralelo en inversa ( fly-back) con motores

La mejor explicación que he encontrado este en este video muy visual

[#183: Why diodes are
used around relay coils: Back to Basics on flyback or snubber diodes](https://youtu.be/c6I7Ycbv8B8?si=-LzSIEa1JaFiiLit)

##### Explicación resumida:

Los diodos de fly-back (o de retorno) se utilizan con motores y cargas inductivas **para proteger los componentes electrónicos de control (como transistores, MOSFETs o relés) contra picos de alto voltaje destructivos.** 

Cuando el circuito que incluye al motor  (o relé),  se apaga, la bobina del motor (o rele) libera la energia magnética acumulada, generando una corriente inversa peligrosa que el diodo disipa. 

**Razones clave para usarlos:**

- **Protección de Componentes:** Evita que el pico de voltaje ("flyback" o fuerza contraelectromotriz) dañe transistores, microcontroladores o interruptores al apagar el motor.
- **Absorción de Energía:** La bobina del motor intenta mantener el flujo de corriente; el diodo, colocado en antiparalelo, proporciona un camino seguro para esta energía.
- **Estabilidad del Circuito:** Reduce el ruido eléctrico y chispazos en interruptores mecánicos, aumentando la vida útil del sistema.

**Cómo conectarlo:**  

    Se debe conectar en paralelo a la bobina del motor, con el cátodo (la parte con la línea) al positivo y el ánodo al negativo, asegurando que quede en **polarización inversa** durante el funcionamiento normal

#### Programa

Usaremos el programa que produce una onda PWM por un pin y puede graduar su 'ciclo de trabajo' como un porcentaje. Solo **hay que cambiar el GPIO al GPIO15**

[R2526CL9_ExPWM_inp100_v1.py](R2526CL9_ExPWM_inp100_v1.py)

---

### 2.Montaje M#1- Control de motor con chip TA6586

Habrá 2 versiones de programa :

- Programa 1.0 : No velocidad ( será 100%) / Si sentido de giro
- Programa 2.0 con PWM : SI velocidad / Si sentido de giro

Pero el montaje HW es CASI el mismo ( ver tutorial SF)

Cambios :

GPIO14  -> pin 1 : BI

GPIO15 -> pin 2 : FI

Condensador para evitar el jitter de 100 nF

    Jitter : ruido eléctrico que provoca resets, lecturas erráticas o vibraciones irregulares) suele venir del ruido de conmutación del motor (escobillas + inductancia)

    Lo ideal es soldarlo a los oines del motor

![](./doc/pico_motorTA6586_bb.png)

#### Programa NoV1.0 : No se controla la velocidad ( será 100%) / Si se controla el sentido de giro

[R2526CL10motorCC_6586NoV_1.py](R2526CL10motorCC_6586NoV_1.py)

En un bucle sin fin, se van al tenrnado cilos de 2 seg de giro horario  - stop 5 seg - giro anti-horario 2 seg. El bucle esta dentro de un try-except para parar con control-D o "stop" de thonny , de forma que el motor se para antes de cerrar el programa.

#### Programa Vel2.0 : Se controla la velocidad por PWM  / Se controla el sentido de giro

[R2526CL10motorCC_6586Vel_2_0.py](R2526CL10motorCC_6586Vel_2_0.py)

1- Observar el cambio en las funciones de avanzar  retroceder, ver el uso de PWM

    CUIDADO : no se deben poner BI y FI en 100% de dutty simultáneamente

2- Los comandos de avanzar / retroceder / parar  , asi como el valor de la velocidad se introducen manualmente 

    Observar las while para check de lo introducido

La evolución natural de este programa es a un control más intuitivo con Rotary encoder y pulsadores 

---

### M#2- Control con integrado TA6586 + Display SH1106 y Rotary encoder

- programa 1.0 : SI velocidad con R. Encoder SIN cambio de sentido 
- programa 2.0 : SI velocidad con R. Encoder  SIN cambio de sentido + display
- programa 3.0 : SI velocidad con R. Encoder +  cambio de sentido con pulsador + display

Hay que repasar la clase del Rotary encoder 

[GitHub - Jcspoza/2425CL10_DisplayGrafSH1106: 1ros pasos con el Display grafico mono SH1106 128x64 · GitHub](https://github.com/Jcspoza/2425CL10_DisplayGrafSH1106)

#### M#2.1 SI velocidad con R. Encoder SIN cambio de sentido

Es un programa muy básico porque las librerías del RE son muy versátiles y solo configurando opciones quitan mucha programación

IMPORTANTE : instalar en PICO _ /W /2W las dos librerias necesarioas para RE

[rotary.py](rotary.py)

[rotary_irq_rp2.py](rotary_irq_rp2.py)

Programa 1.0

[R2526CL10motorCC_6586VelRE_1_0.py](R2526CL10motorCC_6586VelRE_1_0.py)

---

## Tabla resumen de programas

Todos los programas en microPython

| Programa                                                               | Montaje | HW si Robotica y Notas                          | Objetivo de Aprendizaje              |
| ---------------------------------------------------------------------- | ------- | ----------------------------------------------- | ------------------------------------ |
| [R2526CL9_ExPWM_inp100_v1.py](R2526CL9_ExPWM_inp100_v1.py)             | Mon#0   | programa básico, velocidad por input            | solo control de la velocidad por PWM |
| [R2526CL10motorCC_6586NoV_1.py](R2526CL10motorCC_6586NoV_1.py)         | Mon#1   | programa básico - n velocidad                   | chip TA6586 uso básico               |
| [R2526CL10motorCC_6586Vel_2_0.py](R2526CL10motorCC_6586Vel_2_0.py)     | Mon#1   | programa medio - control de velocidad y sentido | chip TA6586 uso con PWM              |
| [R2526CL10motorCC_6586VelRE_1_0.py](R2526CL10motorCC_6586VelRE_1_0.py) | Mon#2.1 | Requiere librerias RE                           |                                      |
| [rotary.py](rotary.py)                                                 |         | Libreria RE 1                                   |                                      |
| [rotary_irq_rp2.py](rotary_irq_rp2.py)                                 |         | Libreria RE 2                                   |                                      |

---

## TO DO y Notas
