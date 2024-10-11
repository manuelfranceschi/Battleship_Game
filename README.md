# Battleship:

Juego de hundir la flota con Python

Actualizaciones:
1. En la funcion crear_barco:
    - Que no se pueda crear un barco que se salga del tablero, mediante recursividad.
2. En la función colocar_barcos:
    - Se crean flotas de barcos con esloras especificas
    - Mediante recursividad, si las coordenadas de los barcos se juntan, se vuelve a llamar la función para que cree nuevamente otra flota
3. En la funcion disparar():
    - Ahora se le pasan 3 argumentos: la casilla, el tablero de ataques y el tablero enemigo. así podrá comprobar que si en el tablero del enemigo se encuentra una posicion ocupada cuando ataquemos nos lo marque con una X, en caso contrario EN LOS DOS tableros se mostrará una A de que hemos fallado
4. Funciones varias:
    - Funcion para pasar las coordenadas que escribe al usuario a una tupla de dos elementos. Falta añadir comprobaciones al string que se pide
    - Funcion para imprimir todos los tableros de un jugador e indicando cual es cada uno de los dos para mejor experiencia de usuario. Es interesante imprimir los 4 tableros cuando haya un ganador y ver como quedaron los tableros con sus disparos.
      
Cosas que se pueden mejorar en el programa:
1. Creacion de clases para inicializar objetos, ejemplo: los jugadores, tableros, partidas… haría el codigo mucho más legible y óptimo
2. Funcion que compruebe que si un barco en sus coordenadas todos  sus valores son X, que se elimine.
3. De momento, la ejecución de la partida no existe. Sigue jugando hasta el fin. La manera que creo mas relevante es si el jugador se queda sin barcos.
4. Comprobaciones: Al pedir una coordenada, no se comprueba si el usuario haya escrito bien los caracteres o no, ni si son numeros propiamente dichos.
5. En ocasiones, cuando ataca el bot, no se marca como X la posicion del jugador. Comprobar
6. Más tiempo para desarrollar este proyecto: El cual veo super util para probar clases y objetos y más cosas interesantes.
