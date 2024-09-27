import utils 

# Se le pide nombre al usuario
nombre = input("Hola! Bienvenido a mi juego de hundir la flota. Dime tu nombre:")
print(f"Vale {nombre}, empezamos!")

# Elige el tamaño del tablero para cada uno de los tableros
print("Opciones de partida:")
tamagno = int(input("Tamaño del tablero:"))

tablero_usuario_ataques = utils.crear_tablero(tamagno)
tablero_usuario_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))
usuario_turno = True
usuario_barcos = len(tablero_usuario_barcos)


tablero_bot_ataques = utils.crear_tablero(tamagno)
tablero_bot_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))
bot_turno = False
bot_barcos = len(tablero_bot_barcos)

# Empieza la partida

jugando = False
# Para salir puede aplicarse recursividad de una funcion o
# while usuario_barcos > 0 or bot_barcos > 0:
while jugando == False:
    # Turno Jugador
    while usuario_turno == True:
        utils.imprimir_tableros(tablero_usuario_ataques, tablero_usuario_barcos)
        print("Turno Jugador")
        coordenada = utils.pasar_a_coordenadas(input("Escribe unas coordenadas (x,y)"))
        print(coordenada)

        utils.disparar(coordenada, tablero_usuario_ataques, tablero_bot_barcos)
        
        if tablero_usuario_ataques[coordenada] == "X":
            #utils.eliminar_barco(tablero_bot_barcos)
            usuario_turno = True
        else:
            usuario_turno = False
            bot_turno = True

    # Turno Bot
    while bot_turno == True:
        print("Turno Bot")
        coordenada = tuple(utils.crear_barco(1)[0]) # Reutilizacion codigo
        utils.disparar(coordenada, tablero_bot_ataques, tablero_usuario_barcos)
        
        if tablero_bot_ataques[coordenada] == "X":
            bot_turno = True
        else:
            bot_turno = False
            usuario_turno = True
            



