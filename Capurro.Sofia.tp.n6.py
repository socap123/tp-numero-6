""" Trabajo Practico N°6
Nombre y Apellido: Capurro Sofia
Comisión: Jueves - virtual
tips:
- para comentar codigo se usa # o comillas triples 
- si se usa vscode, se puede usar el comando ctrl+k, ctrl+c
"""

"""
Ejercicio 01: Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3). 
"""

# def redondear(num):
#     if num - int(num) >= 0.5:
#         return int(num) + 1
#     else:
#         return int(num)

# print(redondear(3.7))
# print(redondear(8.49999)) 

"""
Ejercicio 02: Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado.
"""


# def redondear(num):
#     if num - int(num) >= 0.5:
#         return int(num) + 1
#     else:
#         return int(num)


# def suma_decimales(a, b):
#     resultado = a + b
#     return redondear(resultado)

# print(suma_decimales(3.7, 2.3))  # Salida: 6

"""
Ejercicio 03: Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema.

"""
# from datetime import datetime

# fecha_hora_actual = datetime.now()

# print("Fecha y hora actuales: ", fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S"))

# El formato "%Y-%m-%d %H:%M:%S" significa:

# - %Y: Año con cuatro dígitos
# - %m: Mes con dos dígitos
# - %d: Día del mes con dos dígitos
# - %H: Hora en formato 24 horas con dos dígitos
# - %M: Minutos con dos dígitos
# - %S: Segundos con dos dígitos



"""
Ejercicio 04: Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito).
"""

# import random

# def numero_par_azar():
#     return random.choice([2, 4, 6, 8, 10])

# print(numero_par_azar())


"""
Ejercicio 05:  Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica.
"""
# import random

# def bola_magica():
#     respuestas = [
#         "Es seguro que sí",
#         "Las chances son buenas",
#         "Puedes contar con ello",
#         "Pregúntame de nuevo más tarde",
#         "Concéntrate y pregunta de nuevo",
#         "No veo con claridad, intenta de nuevo",
#         "Mi respuesta es no",
#         "Mis fuentes me dicen que no"
#     ]
#     return random.choice(respuestas)

# print("¡Haz tu pregunta a la bola mágica!")
# pregunta = input()
# print("La bola mágica dice: ", bola_magica())

"""
Ejercicio 06: Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores (pista: use el módulo time)
"""
# import time

# inicio = time.time()

# from datetime import datetime

# fecha_hora_actual = datetime.now()
# print("Fecha y hora actuales: ", fecha_hora_actual.strftime("%Y-%m-%d %H:%M:%S"))


# fin = time.time()

# tiempo_ejecucion = fin - inicio
# print("Tiempo de ejecución: ", tiempo_ejecucion, "segundos")


"""
Ejercicio 07: Sorteo: Escriba un programa que simule un sorteo donde
toman uno o más papeles al azar de un pozo para elegir los ganadores.
"""
# import random

# def sorteo(papeles, num_ganadores):
#     return random.sample(papeles, num_ganadores)


# papeles = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# num_ganadores = 3 

# ganadores = sorteo(papeles, num_ganadores)
# print(f"Ganadores: {ganadores}")


"""
Ejercicio 08: Escriba una función que pida al usuario ingresar su fecha de
nacimiento y sea capaz de devolver la cantidad de días desde su
nacimiento hasta hoy.

"""
# from datetime import datetime

# def calcular_dias_desde_nacimiento():
   
#     fecha_nacimiento_str = input("Ingrese su fecha de nacimiento (en formato YYYY-MM-DD): ")
    
#     try:
#         fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d")
#     except ValueError:
#         print("El formato de la fecha es incorrecto. Por favor, use el formato YYYY-MM-DD.")
#         return
    
#     fecha_actual = datetime.now()
    
#     diferencia = fecha_actual - fecha_nacimiento
#     dias_transcurridos = diferencia.days
    
#     print(f"Han pasado {dias_transcurridos} días desde su nacimiento.")

# calcular_dias_desde_nacimiento()
 

"""
Ejercicio 09:  Implemente el programa del ejercicio 6 usando un diccionario.
"""
# import time

# def operacion_con_diccionario():
#     diccionario = {}
#     for i in range(1000000):
#         diccionario[i] = i * 2
#     total = 0
#     for i in range(1000000):
#         total += diccionario.get(i, 0)
#     return total

# inicio = time.time()

# operacion_con_diccionario()

# fin = time.time()

# tiempo_ejecucion = fin - inicio

# print(f"El tiempo de ejecución de la operación con el diccionario es: {tiempo_ejecucion} segundos")
