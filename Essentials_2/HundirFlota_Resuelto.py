class Juegos:
    pass

class JuegoMesa(Juegos):
    pass

class JuegoMesaTablero(JuegoMesa):
    def __init__(self, tam_filas, tam_columnas, contenido):
        self.__tamaño_filas = tam_filas
        self.__tamaño_columnas = tam_columnas
        self.__tablero = self.__inicializar(contenido)
        
    def __inicializar(self, contenido):
        #self._tablero = [ [contenido for columna in range(self._tamaño_columnas)] for fila in range(self._tamaño_filas)]
        return [ [contenido for columna in range(self.__tamaño_columnas)] for fila in range(self.__tamaño_filas)]

    def imprimir(self):
        for fila in self.__tablero:
            print(fila)
    
    def insertar(self, fila, columna, contenido):
        self.__tablero[fila][columna] = contenido

    def recuperar(self, fila, columna):
        return self.__tablero[fila][columna]

    def recuperar_tamaño_tablero(self):
        return self.__tamaño_filas, self.__tamaño_columnas

class HundirFlota(JuegoMesaTablero):
    def __init__(self, filas, columnas, contenido):
        super().__init__(filas, columnas, contenido)

    def insertar_barco(self, fila, columna, tamano, ubicacion):
        nombre_fila = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_fila = nombre_fila.find(fila)
        
        if ubicacion == "H":
            for pos in range(tamano):
                self.insertar(num_fila,columna + pos - 1,"x")
        else:
            for pos in range(tamano):
                self.insertar(num_fila + pos,columna - 1,"x")

    def jugar(self, fila, columna):
        nombre_fila = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_fila = nombre_fila.find(fila)
        
        tiro = self.recuperar(num_fila,columna - 1)
        if tiro == ".":
            self.insertar(num_fila,columna - 1,"a")
            print("Agua")
        elif tiro == "x":
            self.insertar(num_fila,columna - 1,"t")
            print("Tocado")
        elif tiro in ("a","t"):
            print("Tiro repetido")

    def barcos_hundidos(self):
        tamFilas, tamColumnas = self.recuperar_tamaño_tablero()
        for fila in range(tamFilas):
            for columna in range(tamColumnas):
                if self.recuperar(fila,columna) == "x":
                    return False
        return True

class Ajedrez(JuegoMesaTablero):
    def __init__(self, filas, columnas, contenido):
        super().__init__(filas, columnas, contenido)


juego_hf = HundirFlota(10,10,".")
juego_hf.imprimir()

#juego_aj = ajedrez(8,8,".")
#juego_aj.imprimir()

while True:
    try:
        input_fila = input("Introduce fila donde ubicar el barco (A-J): ").upper()
        if input_fila not in ("ABCDEFGHIJ"):
            input_fila = "A"
        nombre_fila = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num_fila = nombre_fila.find(input_fila)

        input_col = int(input("Introduce columna donde ubicar el barco (0 - fin): "))
        if input_col == 0:
            break
        
        input_tam = int(input("Introduce el tamaño del barco (1-4): "))
        input_pos = input("Introduce posición Horizontal/Vertical: ").upper()
        if input_pos not in ("V","H"):
            input_pos = "H"

        juego_hf.insertar_barco(input_fila, input_col, input_tam, input_pos)
        juego_hf.imprimir()
    except ValueError:
        print("Debe ser un valor numérico!")
    #except:
        #print("Error desconozido")

print("--------------")

while True:
    casilla = input("Introduce casilla a jugar (s - salir): ").upper()
    try:
        fila = casilla[0]
        if fila != "S":
            columna = int(casilla[1])
            juego_hf.jugar(fila, columna)
            juego_hf.imprimir()

            if juego_hf.barcos_hundidos():
                print("TODOS los barcos hundidos! Has ganado la partida!")
                break
            else:
                print("Aun hay barcos sin hundir!")
    except:
        print("Error, vuelve a intentarlo!!!")
        