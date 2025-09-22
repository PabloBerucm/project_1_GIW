"""
TODO: rellenar

Asignatura: GIW
Práctica 1
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""


# Ejercicio 1

def dimension(matriz):
    #si la matriz está vacía devuelve none
    if not matriz:
        return (None, None)
    #busca las filas de la matriz
    n_filas = len(matriz)
    #cogerá la fila con más elementos de la matriz que será el número de columnas
    n_columnas = max((len(fila) for fila in matriz))
    return (n_filas, n_columnas)



def es_cuadrada(matriz):
    #busca las filas de la matriz
    n_filas = len(matriz)
    #cogerá la fila con más elementos de la matriz que será el número de columnas
    n_columnas = max(len(fila) for fila in matriz)
    #return True if n_filas == n_columnas else False
    return n_filas == n_columnas


def es_simetrica(matriz):
    for i in matriz:
        for j in matriz:
            if matriz[i][j] != matriz [j][i]:
                return False
    return True



def multiplica_escalar(matriz, k):
    ...

def suma(matriz1, matriz2):
    ...


# Ejercicio 2
def validar(grafo):
    ...

def grado_entrada(grafo, nodo):
    ...

def distancia(grafo, nodo):
    ...
   

#a partir de aquí está el código para probar las funciones
matriz1 = [[1, 0, 2, 5], 
           [0, 3, 3, 5], 
           [1, 2, 2, 5]
        ]

matriz2 = [[1, 0, 1], 
           [0, 3, 2], 
           [1, 2, 2]
        ]

print(dimension(matriz1))
print(dimension(matriz2))

print('es cuadrada' if es_cuadrada(matriz1) else 'no es cuadrada')
