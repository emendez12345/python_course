# def saludar():
#     print('Hola, bienvenido')
# saludar()    
# Representación del tablero con una matriz
# Cada pieza se representa con una letra (P: Peón, R: Torre, N: Caballo, B: Alfil, Q: Reina, K: Rey)
# Mayúsculas para blancas, minúsculas para negras

def crear_tablero():
    """Crea y devuelve el tablero inicial de ajedrez como una matriz."""
    return [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

def imprimir_tablero(tablero):
    """Imprime el tablero en la consola."""
    for fila in tablero:
        print(" ".join(fila))
    print()

def mover_pieza(tablero, inicio, destino):
    """Mueve una pieza en el tablero si la jugada es válida."""
    x1, y1 = inicio  # Posición inicial
    x2, y2 = destino  # Posición destino
    
    # Verificar que hay una pieza en la casilla de origen
    if tablero[x1][y1] == ".":
        print("No hay pieza en la posición inicial.")
        return False
    
    # Mover la pieza
    tablero[x2][y2] = tablero[x1][y1]
    tablero[x1][y1] = "."
    return True

def jugar():
    """Función principal que controla el flujo del juego."""
    tablero = crear_tablero()
    turno = "blancas"
    
    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {turno}")
        
        try:
            # Pedir coordenadas de la pieza y el destino
            inicio = tuple(map(int, input("Ingresa la fila y columna de la pieza a mover (ej: 6 0): ").split()))
            destino = tuple(map(int, input("Ingresa la fila y columna de destino (ej: 4 0): ").split()))
            
            # Si el movimiento es válido, cambia de turno
            if mover_pieza(tablero, inicio, destino):
                turno = "negras" if turno == "blancas" else "blancas"
        except Exception:
            print("Entrada inválida. Intenta de nuevo.")

if __name__ == "__main__":
    jugar()

