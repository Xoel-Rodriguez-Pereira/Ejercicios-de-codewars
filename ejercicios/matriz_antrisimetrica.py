def esAntisimetrica (matriz):

    CERO = 0
    for fila in range(len(matriz)):

        if len(matriz[fila]) != len(matriz):
            return False

        for columna in (range(len(matriz[fila]))):
            
            # if fila == columna and matriz[fila][columna] != CERO:
            #   return False
            
            if matriz[fila][columna] != -matriz[columna][fila]: # no es necesario comprobar si matriz[fila][columna] es 0, porque si no lo es 'item != -item'
                return False
    
    return True



if __name__ == '__main__':

    assert esAntisimetrica([[0, 1, 2], 
                            [-1, 0, 3], 
                            [-2, -3, 0]])   
    #>>> True

    assert esAntisimetrica([[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]])
    #>>> True

    assert not esAntisimetrica([[0, 1, 2], 
                                [-1, 0, -2], 
                                [2, 2,  3]])
    #>>> False

    assert not esAntisimetrica([[1, 2, 5],
                                [0, 1, -9],
                                [0, 0, 1]])
    #>>> False

    assert esAntisimetrica([[0, 1, 10],
                            [-1, 0, 4],
                            [-10, -4, 0]])
    #>>> True

    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert)

    matriz4 = [[1,0,0,0],
               [0,1,1,0],
               [0,0,0,1]]

    assert not esAntisimetrica(matriz4)
    #>>>False

    matriz5 = [[1,0,0,0,0,0,0,0,0]]

    assert not esAntisimetrica(matriz5)
    #>>>False 