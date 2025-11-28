def esMatrizIdentidad (matriz):

    CERO = 0
    UNO = 1
    fila = 0
    while fila < len(matriz):

        if len(matriz[fila]) != len(matriz):
            return False

        columna = 0
        while columna < len(matriz[fila]):
            
            if fila == columna and matriz[fila][columna] != UNO:
                return False
            
            elif fila != columna and matriz[fila][columna] != CERO:
                return False

            columna += 1

        fila += 1
        
    return True


if __name__ == '__main__':
    matrix1 = [[1,0,0,0],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]]
    assert esMatrizIdentidad(matrix1)
    #>>>True

    matrix2 = [[1,0,0],
               [0,1,0],
               [0,0,0]]

    assert not esMatrizIdentidad(matrix2)
    #>>>False

    matrix3 = [[2,0,0],
               [0,2,0],
               [0,0,2]]

    assert not esMatrizIdentidad(matrix3)
    #>>>False

    matrix6 = [[1,0,0,0],  
               [0,1,0,2],  
               [0,0,1,0],  
               [0,0,0,1]]

    assert not esMatrizIdentidad(matrix6)
    #>>>False

    matrix7 = [[1, -1, 1],
               [0, 1, 0],
               [0, 0, 1]]
    assert not esMatrizIdentidad(matrix7)
    #>>>False           


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

    matrix4 = [[1,0,0,0],
               [0,1,1,0],
               [0,0,0,1]]

    assert not esMatrizIdentidad(matrix4)
    #>>>False

    matrix5 = [[1,0,0,0,0,0,0,0,0]]

    assert not esMatrizIdentidad(matrix5)
    #>>>False 