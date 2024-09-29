import utils 
import time

# Se le pide nombre al usuario
nombre = input("Hola! Bienvenido a mi juego de hundir la flota. Dime tu nombre:")
print(f"Vale {nombre}, empezamos!")

# Elige el tamaño del tablero para cada uno de los tableros
print("Opciones de partida:")
tamagno = int(input("Tamaño del tablero:"))
#Datos usuario
tablero_usuario_ataques = utils.crear_tablero(tamagno)
tablero_usuario_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))
usuario_turno = True
usuario_barcos = len(tablero_usuario_barcos)
usuario_puntos = 0
# Datos bot
tablero_bot_ataques = utils.crear_tablero(tamagno)
tablero_bot_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))
bot_turno = False
bot_barcos = len(tablero_bot_barcos)
bot_puntos = 3
# Empieza la partida

"""
Se ha realizado un sistema de puntuación sencillo para que la partida pueda terminar, de momento es una solución para salir del bucle
en el que se encuentra el programa
"""
# Para salir puede aplicarse recursividad de una funcion o
# while usuario_barcos > 0 or bot_barcos > 0:
while usuario_puntos > 3 or bot_puntos > 3:
    # Turno Jugador
    while usuario_turno == True:
        utils.imprimir_tableros(tablero_usuario_ataques, tablero_usuario_barcos)
        print("Turno Jugador")
        print(f"Puntos jugador: {usuario_puntos}")
        coordenada = utils.pasar_a_coordenadas(input("Escribe unas coordenadas (x,y)"))
        print(coordenada)

        utils.disparar(coordenada, tablero_usuario_ataques, tablero_bot_barcos)
        
        
        if tablero_usuario_ataques[coordenada] == "X":
            print("Le has dado!")
            time.sleep(2)
            usuario_puntos += 1
            usuario_turno = True
        else:
            print("Has fallado!")
            time.sleep(2)
            usuario_turno = False
            bot_turno = True

    # Turno Bot
    while bot_turno == True:
        print("Turno Bot")
        print(f"Puntos bot: {bot_puntos}")
        coordenada = tuple(utils.crear_barco(1)[0]) # Reutilizacion codigo
        utils.disparar(coordenada, tablero_bot_ataques, tablero_usuario_barcos)
        if tablero_bot_ataques[coordenada] == "X":
            print("Le has dado!")
            time.sleep(2)
            bot_puntos += 1
            bot_turno = True
        else:
            print("Has fallado!")
            time.sleep(2)
            bot_turno = False
            usuario_turno = True

if usuario_puntos > bot_puntos:
    print(f"{nombre}, has ganado!!")
else:
    print(f"Te ha ganado el bot, {nombre} :/. \n ya habrá suerte la proxima")
            



