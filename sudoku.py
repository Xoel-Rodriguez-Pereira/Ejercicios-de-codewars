def comprobar_cuadrado(sudoku):

    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        if len(sudoku[fila]) != numero_filas:

            return False
        
        else:

            fila += 1

    return True


def comprobar_validez_numero(sudoku):

    MAX_RANGE = len(sudoku) + 1
    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        columna = 0
        while columna < numero_filas:

            if sudoku[fila][columna] not in range (1, MAX_RANGE):

                return False
            
            columna += 1

        fila += 1
            
    return True


def comprobar_fila(sudoku):

    numero_filas = len(sudoku)

    fila = 0
    while fila < numero_filas:

        fila_index = 0

        while fila_index < numero_filas:

            if sudoku[fila].count(sudoku[fila][fila_index]) > 1:

                return False
            
            fila_index += 1

        fila += 1

    return True


def comprobar_columna(sudoku):

    numero_columnas = len(sudoku)

    columna = 0
    while columna < numero_columnas:

        lista_elementos_columna = []

        columna_index = 0
        while columna_index < numero_columnas:

            lista_elementos_columna += [sudoku[columna_index][columna]]

            if lista_elementos_columna.count(sudoku[columna_index][columna]) > 1:

                return False

            columna_index += 1

        columna += 1

    return True


def check_sudoku(sudoku):

    return comprobar_cuadrado(sudoku) and comprobar_validez_numero(sudoku) and comprobar_fila(sudoku) and comprobar_columna(sudoku)


if __name__ == "__main__":

    correcto = [[1, 2, 3], [2, 3, 1], [3, 1, 2]]
    

    fila_invalida = [[1, 2, 3, 4], [2, 3, 1, 3], [3, 1, 2, 3], [4, 4, 4, 4]]
    

    columna_invalida = [[1, 2, 3, 4], [2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 1, 2]]

    rango_sobrepasado = [
        [1, 2, 3, 4, 5],
        [2, 3, 1, 5, 6],
        [4, 5, 2, 1, 3],
        [3, 4, 5, 2, 1],
        [5, 6, 4, 3, 2],
    ]
    

    no_numeros = [["a", "b", "c"], ["b", "c", "a"], ["c", "a", "b"]]

    no_entero = [[1, 1.5], [1.5, 1]]

    no_cuadrado = [[1, 0, 0, 0], [0, 1, 0], [0, 0, 0, 1]]

    lista_vacia = [[]]

### TEST TRUE ###
    assert comprobar_cuadrado(correcto) is True

    assert comprobar_fila(correcto) is True
    
    assert comprobar_columna(correcto) is True
    
### TEST FALSE ###
    assert comprobar_cuadrado(no_cuadrado) is False
    assert comprobar_cuadrado(lista_vacia) is False

    assert comprobar_fila(fila_invalida) is False

    assert comprobar_validez_numero(rango_sobrepasado) is False
    assert comprobar_validez_numero(no_numeros) is False
    assert comprobar_validez_numero(no_entero) is False

## TODOS LOS TEST PARA check_sudoku ##
    assert check_sudoku(correcto) is True
    assert check_sudoku(fila_invalida) is False
    assert check_sudoku(columna_invalida) is False
    assert check_sudoku(rango_sobrepasado) is False
    assert check_sudoku(no_numeros) is False
    assert check_sudoku(no_entero) is False
    assert check_sudoku(no_cuadrado) is False
    assert check_sudoku(lista_vacia) is False
