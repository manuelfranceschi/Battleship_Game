import numpy as np
import random
# Funciones tableros y barcos
def crear_tablero(tamaño):
    tablero = np.full((tamaño,tamaño), "_")
    return tablero

def colocar_barco(barco, tablero):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero

def disparar(casilla, tablero):
    if tablero[casilla] == "O":
        print("Tocado")
        tablero[casilla] = "X"
    else:
        print("Agua")
        tablero[casilla] = "A"
    return tablero

def crear_barco(eslora): #eslora es la longitud del barco
    casilla_0 = (random.randint(0,9), random.randint(0,9)) #casilla en la que empezará
    orientacion = random.choice(["Vertical", "Horizontal"]) #orientacion por donde se creara el barco

    barco = [casilla_0]
    casilla = casilla_0
    while len(barco) < eslora:
        if orientacion == "Vertical":
            casilla = (casilla[0]+1, casilla[1])
            barco.append(casilla) # Vertical
        else:
            casilla = (casilla[0], casilla[1]+1)
            barco.append(casilla) # Horizontal         
    
    for x,y in barco:
        if x == 10 or y == 10:
            return crear_barco(eslora)
    return barco

def colocar_barcos(tablero):
    flota =[crear_barco(2),crear_barco(2),crear_barco(2), crear_barco(3), crear_barco(3), crear_barco(4)]
    for barco in flota:
        for x, y in barco:
            if tablero[x,y] == "O":
                colocar_barcos(tablero)
            else:
                for barco in flota:
                    colocar_barco(barco, tablero)
                return tablero
# Funciones juego         
def pasar_a_coordenadas(coord):
    coord = coord.split(",")
    coord = [int(numero) for numero in coord]
    coord = tuple(coord)
    return coord           

def imprimir_tableros(tablero_ataques, tablero_usuario):
    print(f"{tablero_ataques} \n {"Tablero ataques".center(40)} \n \n {"*" * 43} \n \n{tablero_usuario} \n {"Tablero jugador".center(40)}")


def disparar(casilla, tablero_usuario_ataques, tablero_barcos_enemigo):
    if tablero_barcos_enemigo[casilla] == "O":
        print("Tocado")
        tablero_barcos_enemigo[casilla],tablero_usuario_ataques[casilla] = "X", "X"
    else:
        print("Agua")
        tablero_barcos_enemigo[casilla],tablero_usuario_ataques[casilla] = "A", "A"
    return tablero_usuario_ataques, tablero_barcos_enemigo

# Funcion que compruebe que si un barco en sus coordenadas EN EL MAPA todos  sus valores son X, que se elimine.
#def eliminar_barco(tablero_enemigo):
    #for i, value in enumerate(tablero_enemigo):
      #  if tablero_enemigo[i] == "X":
        #    print(i, value)
            #list(tablero_enemigo).pop(i)

# Crear Clases
            
# Tablero: Ya que habrá uno para cada jugador, y dos para comparar
            
# Jugador: Ya que cada jugador tendrá su tablero, tendrá n barcos que 
# pueden ser destruidos, acciones como disparar, etc.
# Partida: Cada partida que se cree puede tener:
# 1. Jugadores (O jugador)
# 2. Tablero
# 3. Numero de barcos
# 4. Opciones de dificultad
# 5. Salir, reanudar partida, etc.