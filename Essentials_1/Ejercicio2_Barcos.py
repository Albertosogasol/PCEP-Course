"""
Juego de los barcos. 
Normas:
    - Tablero de 10x10 (A-J filas / 1-10 columnas)
    - El tablero de juego del orndeador se rellande forma automatica sin intervención del usuario

Tabajar con funciones para crear el tablero, definir posición de barcos, etc...
"""
#FUNCIONES

#Dibuja el tablero vacío
def empty_board(board_rows, board_cols):
    for i in board_rows:
        print(i + " [", end=" ")
        for j in board_cols:
            print("'.',", end=" ")
        print("]")

#Dibuja el tablero con el disparo pasado por parámetro
def refresh_board(board):
    for i in range(len(board)):
        print(" [", end=" ")
        for j in range(len(board[0])):
            if board[i][j] == ".":
                print("'.',", end=" ")
            elif board[i][j] == "A":
                print("'A',", end=" ")
            elif board[i][j] == "T":
                print("'T',", end=" ")
            elif board[i][j] == "X":
                print("'X',", end=" ")                
        print("]")
            
     
#Numero de filas y columnas
list_rows=["A","B","C","D","E","F","G","H","I","J"]
list_cols=[1,2,3,4,5,6,7,8,9,10]

#Dibujamos el tablero vacío
empty_board(list_rows,list_cols)

#Posición de un barco
ship_x=3
ship_y=4

#Comienza el juego
row_shot = 0
col_shot = 0

#Verificación de tocado
x_hit = False
y_hit = False

board_status = [['.' for _ in range(10)] for _ in range(10)]

while True:
    if x_hit and y_hit == True:
        print("HUNDIDO!")
        print("Juego finalizado!")
        break

    row_shot=int(input("Introduce la fila de disparo (s - Salir): "))
    col_shot=int(input("Introduce la columna de disparo (s - Salir): "))

    if row_shot == ship_y or col_shot == ship_x:
        print("Tocado!")
        if row_shot == ship_y and col_shot == ship_x:
            y_hit = True
            x_hit = True
            board_status[row_shot-1][col_shot-1] = "X"
            refresh_board(board_status)
        elif row_shot == ship_y:
            y_hit = True
            board_status[row_shot-1][col_shot-1] = "T"
            refresh_board(board_status)
        elif col_shot == ship_x:
            x_hit = True
            board_status[row_shot-1][col_shot-1] = "T"
            refresh_board(board_status)
    elif row_shot != ship_y and col_shot != ship_x:
        print("Agua!")
        board_status[row_shot-1][col_shot-1] = "A"
        refresh_board(board_status)
            




