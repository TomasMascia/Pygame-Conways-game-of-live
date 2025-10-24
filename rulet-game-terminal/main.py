# JUEGO DE RULETA, CON APUESTA DE DINERO Y DISEÑO DE TABLA DE NUMEROS
# TOMÁS MASCIA

import random
import time

AMARILLO = "\033[33m"
RESET = "\033[0m"
VERDE = "\033[32m"

fila1 = [3,6,9,12,15,18,21,24,27,30,33,36]
fila2 = [2,5,8,11,14,17,20,23,26,29,32,35]
fila3 = [1,4,7,10,13,16,19,22,25,28,31,34]

diccio = {}

# Funcion para poder ver todas las apuestas que hizo el usuario
# Esta funcion la realice para poder imprimir los numeros con sus respectivas apuestas
def imprimir_apuestas(lista):
    for x in lista:
        print(f"Número {x} --> ${lista[x]}")
    print()


# VALIDACION DE SI GANA O NO
def validar_ganar(diccio, numero_elegido, dinero_restante):
    print(f"EL numero ganador fue: {VERDE}{numero_elegido}{RESET}\n")
    total_ganado = 0

    if numero_elegido in diccio:
        apuesta = diccio[numero_elegido]
        ganancia = apuesta * 35
        total_ganado += ganancia + apuesta
        print(f"{VERDE}GANASTE CON EL NUMERO: {numero_elegido}{RESET}")
        print(f"GANASTE ${ganancia}")
    else:
        print("PERDISTE PELOTUDO, DEJA DE PERDER PLATA")

# ESTA FUNCION VALIDA SI EL NUMERO ESTA DENTRO DEL 0 Y DEL 36
def validar_numero_apostado(numero_apostado):
        while numero_apostado > 36 or numero_apostado < 0:
            print("No se puede este numero. No se encuentra en la tabla")
            numero_apostado = int(input("ngrese numero para la apuesta de nuevo: "))

# ESTA FUNCION VALIDA SI EL DINERO INGRESADO NO EXCEDE DEL SALDO QUE TIENE EL USUARIO
def validar_dinero_apostado(saldo, dinero_apostado):
    while dinero_apostado > saldo or dinero_apostado <= 0:
        print("No puede seleccionar este monto ingresado")
        dinero_apostado = int(input("Ingrese monto de la apuesta: "))

# JUEGO DE APUESTA INICIAL SIN NADA
def apuesta(saldo):

    while saldo != 0:
        # seleccion de numero para apostar
        numero_apostado = int(input("Elegir un número del 0 al 36: "))  # valor de key
        validar_numero_apostado(numero_apostado)

        # seleccion de dinero para ese numero
        dinero_apostado = int(input("Cuanto apuesta por este numero: "))  #valor de value
        validar_dinero_apostado(saldo, dinero_apostado)

        diccio[numero_apostado] = dinero_apostado  # guardamos el numero en el diccionario con su respectiva apuesta
    
        saldo = saldo - dinero_apostado 

        while seguir_apostando == "si":

            # validamos de nuevo el numero si esta en la tabla
            numero_apostado = int(input("Elegir un número del 0 al 36: "))
            validar_numero_apostado(numero_apostado)

            # validamos si el monto ingresado sea correcto con lo que le resta de saldo    
            dinero_apostado = int(input("Cuanto apuesta por este numero: "))
            validar_dinero_apostado(saldo, dinero_apostado)
    
            saldo = saldo - dinero_apostado
            seguir_apostando = "no"

            if numero_apostado in diccio:
                diccio[numero_apostado] += dinero_apostado
            else:
                diccio[numero_apostado] = dinero_apostado

        else:
    
            print("\n")
            print("Estas son tus apuestas")
            imprimir_apuestas(diccio)
            print(f"Apusta realizada. Saldo restante: ${saldo}")

            time.sleep(2)
            print("Girando la ruleta...\n")
            time.sleep(2)

    else:
        print("Te quedaste sin saldo. Apostaste todo tu dinero")
        time.sleep(2)
        print("Girando la ruleta...\n")
        time.sleep(2)



# ESTA FUNCION PINTA LAS APUESTAS QUE REALIZO EL USUSARIO
def pintar_numeros(diccionario):
    for numero in diccionario:

        if numero in fila1 or numero in fila2 or numero in fila3:
            return f"{AMARILLO}{numero}"
        else:
            return numero

# ESTA FUNCION PINTA EL NUMERO GANADOR

# REPRESENTACION GRAFICA DE LA TABLA DE NUMEROS

def dibujar_tabla(diccionario = None, numero_ganador = 0):
    for fila in [fila1, fila2, fila3]:
        print("_" * 55)
        for numero in fila:
            if diccionario and numero in diccionario:
                print(f"{AMARILLO}{numero}{RESET} |", end=" ")
            else:
                print(numero,"|", end=" ")
        print()
    print("_" * 55)
    print()



# JUEGO COMPLETO

def juego_completo():

    numero_seleccionado = random.randint(0,36)
    print("TABLA DE NUMEROS:")
    dibujar_tabla(diccio)

    dinero_ingresado = int(input("Ingrese el monto que ingresa al casino: "))
    apuesta(dinero_ingresado)

    saldo_final = validar_ganar(diccio, numero_seleccionado, dinero_ingresado)

    dibujar_tabla(diccio)

    # validacion_ganar(diccio, numero_seleccionado)
    # print(f"El numero ganador fue el {numero_seleccionado}")




juego_completo()