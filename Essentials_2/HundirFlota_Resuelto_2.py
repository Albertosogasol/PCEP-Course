# Definimos la superclase principal
class Game:
    # Método constructor
    def __init__(self, name, players):
        self.name = name
        self.players = players

# Diferentes subclases:
class Table(Game):
    pass

class Sports(Game):
    pass

class Board(Table):
    # Constructor de la clase Board
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

class Cards(Table):
    pass

class SinkFleet(Board):
    # Constructor de SinkFleet
    def __init__(self):
        super().__init__(10, 10)  # Inicializa un tablero de 10x10
        self.start_sink_fleet_game()  # Inicia el juego de hundir la flota

    def start_sink_fleet_game(self):
        # Añade aquí el código del juego de hundir la flota
        tablero = []
        tablero_tam = 10

        def pintar_tablero(tablero, tablero_tam):
            nombre_fila = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            fila = 0
            for fila in range(tablero_tam):
                print(nombre_fila[fila],"", end="")
                print(str(tablero[fila]))

        def insertar_barco(tablero,fila,columna, tamano, ubicacion):
            nombre_fila = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Las cadenas dentro de python se pueden trabajar como listas
            num_fila = nombre_fila.find(fila)

            if ubicacion == "H":
                for pos in range(tamano):
                    tablero[num_fila][columna + pos - 1]="x"
            else:
                for pos in range(tamano):
                    tablero[num_fila + pos][columna - 1]="x"
            return tablero

        def jugar(tablero, fila, columna):
            nombre_fila = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            num_fila = nombre_fila.find(fila)

            tiro = tablero[num_fila][columna - 1]
            if tiro == ".":
                tablero[num_fila][columna - 1] = "a"
                print("Agua")
            elif tiro == "x":
                tablero[num_fila][columna - 1] = "t"
                print("Tocado")
            elif tiro in ("a","t"):
                print("Tiro repetido")
            return tablero

        def barcos_hundidos(tablero, tamano):
            for fila in range(tamano):
                for columna in range(tamano):
                    if tablero[fila][columna] == "x":
                        return False
            return True

        tablero = [ ["." for columna in range(tablero_tam)] for fila in range(tablero_tam)]
        pintar_tablero(tablero,tablero_tam)

        print("--------------")

        tablero = insertar_barco(tablero, "C", 2, 2, "H")
        pintar_tablero(tablero,tablero_tam)

        print("--------------")

        while True:
            casilla = input("Introduce casilla a jugar (s - salir): ").upper()
            fila = casilla[0]
            if fila != "S":
                columna = int(casilla[1])
                tablero = jugar(tablero, fila, columna)
                pintar_tablero(tablero,tablero_tam)

                estado_partida = barcos_hundidos(tablero, tablero_tam)
                if estado_partida == True:
                    print("TODOS los barcos hundidos! Has ganado la partida!")
                    break
                else:
                    print("Esto es el else del final")

class Chess(Board):
    pass

# Variables
game_select = ''

# Código principal
while True:
    print("Bienvenido a juegos de Python. ¿A qué juego desea jugar?")
    game_select = input("H-Hundir la Flota ").upper()
    if game_select != 'H':
        continue
    else:
        current_game = SinkFleet()  # Crear un objeto de SinkFleet
        print("¡Juego de Hundir la Flota creado!")
        break  # Salir del bucle después de crear el juego de hundir la flota
