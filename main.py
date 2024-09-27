import utils 

# Se le pide nombre al usuario
nombre = input("Hola! Bienvenido a mi juego de hundir la flota. Dime tu nombre:")
print(f"Vale {nombre}, empezamos!")

# Elige el tamaño del tablero para cada uno de los tableros
print("Opciones de partida:")
tamagno = int(input("Tamaño del tablero:"))

tablero_usuario_ataques = utils.crear_tablero(tamagno)
tablero_usuario_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))
turno_jugador = True

tablero_bot_ataques = utils.crear_tablero(tamagno)
tablero_bot_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))
turno_bot = False

# Empieza la partida

jugando = False
while jugando == False:
    # Turno Jugador
    while turno_jugador == True:
        utils.imprimir_tableros(tablero_usuario_ataques, tablero_usuario_barcos)

        coordenada = utils.pasar_a_coordenadas(input("Escribe unas coordenadas (x,y)"))
        print(coordenada)

        utils.disparar(coordenada, tablero_usuario_ataques, tablero_bot_barcos)
        
        if tablero_usuario_ataques[coordenada] == "X":
            turno_jugador = True
        else:
            turno_jugador = False
            turno_bot = True

    # Turno Bot
    while turno_bot == True:
        coordenada = tuple(utils.crear_barco(1)[0]) # Reutilizacion codigo
        print(coordenada)

        utils.disparar(coordenada, tablero_bot_ataques, tablero_usuario_barcos)
        
        if tablero_bot_ataques[coordenada] == "X":
            turno_bot = True
        else:
            turno_bot = False
            turno_jugador = True
            



