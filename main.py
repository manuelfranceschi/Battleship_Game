import utils 
"""
6. Escribe el flujo completo del programa, con la dinámica de turnos y 
funcionalidades necesarios para jugar contra la máquina (dispara a tu tablero de 
forma aleatoria). Crea todas las funciones que necesites y aplica todo lo 
aprendido que te sea útil.
"""

# print que presentan el juego al usuario
#print("Hola! Bienvenido a mi juego de hundir la flota.")

# pediremos el nombre al usuario
#nombre = input("Dime tu nombre")

# El juego empieza
#print(f"Vale {nombre}, empezamos!")
#print("Opciones de partida:")

# Se crea el tablero
tamagno = int(input("Tamaño del tablero:"))

tablero_usuario_ataques = utils.crear_tablero(tamagno)
tablero_usuario_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))

tablero_bot_ataques = utils.crear_tablero(tamagno)
tablero_bot_barcos = utils.colocar_barcos(utils.crear_tablero(tamagno))





