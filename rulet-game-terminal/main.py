# JUEGO DE RULETA, CON APUESTA DE DINERO Y DISEÑO DE TABLA DE NUMEROS
# TOMÁS MASCIA

import random
import time

AMARILLO = "\033[33m"
RESET = "\033[0m"

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
def validacion_ganar(diccio, numero, dinero):
    monto_ganado = 0

    if numero in diccio:
        monto_ganado = diccio[numero] * 2

        for montos in diccio:
            monto_ganado = diccio[montos]

        print("GANASTE PAPÁ")
        
    else:
        print("PERDISTE MUCHA PLATA")



# JUEGO DE APUESTA INICIAL SIN NADA
def apuesta(dinero):

    # seleccion de numero para apostar
    numero_apostado = int(input("Elegir un número del 0 al 36: "))  # valor de key
    while numero_apostado > 36 or numero_apostado < 0:
        print("No se puede este numero. No se encuentra en la tabla")
        numero_apostado = int(input("ngrese numero para la apuesta de nuevo: "))

    # seleccion de dinero para ese numero
    dinero_apostado = int(input("Cuanto apuesta por este numero: "))  #valor de value
    while dinero_apostado > dinero or dinero_apostado <= 0:
        print("No puede seleccionar este monto ingresado")
        dinero_apostado = int(input("Ingrese monto de la apuesta: "))

    # guardamos el numero en el diccionario con su respectiva apuesta
    diccio[numero_apostado] = dinero_apostado  #lo coloca en el diccionario de apuestas
    dinero = dinero - dinero_apostado 

    # preguntamos si quiere apostar a otro numero
    seguir_apostando = str(input("Ingrese si quiere apostar otro numero: si/no\n"))

    while seguir_apostando == "si":
            # validamos de nuevo el numero si esta en la tabla
            numero_apostado = int(input("Elegir un número del 0 al 36: "))
            while numero_apostado > 36 or numero_apostado < 0:
                print("No se puede este numero. No se encuentra en la tabla")
                numero_apostado = int(input("ngrese numero para la apuesta de nuevo: "))

            # validamos si el monto ingresado sea correcto con lo que le resta de saldo    
            dinero_apostado = int(input("Cuanto apuesta por este numero: "))
            while dinero_apostado > dinero or dinero_apostado <= 0:
                print("No puede seleccionar este monto ingresado")
                dinero_apostado = int(input("Ingrese monto de la apuesta: "))

            
            dinero = dinero - dinero_apostado

            if numero_apostado in diccio:
                diccio[numero_apostado] += dinero_apostado
            else:
                diccio[numero_apostado] = dinero_apostado
             
            seguir_apostando = str(input("Ingrese si quiere apostar otro numero: si/no\n"))

    else:

        
        print("\n")
        print("Estas son tus apuestas")
        imprimir_apuestas(diccio)

        
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


# REPRESENTACION GRAFICA DE LA TABLA DE NUMEROS

def dibujar_tabla(diccionario = None):
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

    dibujar_tabla(diccio)

    dinero_ingresado = int(input("Ingrese el monto con el que quiere apostar: "))

    apuesta(dinero_ingresado)

    dibujar_tabla(diccio)

    validacion_ganar(diccio, numero_seleccionado)

    print(f"El numero ganador fue el {numero_seleccionado}")

juego_completo()