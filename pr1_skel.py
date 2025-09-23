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
    #se crea la matriz auxiliar para devolver
    matriz_aux = []
    #se recorren todos los elementos de la matriz de la llamada
    for fila in matriz:
        nueva_fila = []
        for x in fila:
            #multiplicamos el número por k y lo metemos en la fila
            nuevo_numero = x*k
            nueva_fila.append(nuevo_numero)
        #metemos la fila en la matriz auxiliar y repetimos hasta acabar con todas las filas
        matriz_aux.append(nueva_fila)
    return matriz_aux

def suma(matriz1, matriz2):
    #Comprobamos que tengan las mismas dimensiones
    dim1 = dimension(matriz1)
    dim2 = dimension(matriz2)
    if(dim1 != dim2): return None

    #creamos una nueva matriz para devolver
    matriz_aux = []
    # Recorremos las filas por índice de fila
    for i in range(len(matriz1)):
        nueva_fila = []

        # Recorremos las columnas por índice de columna
        for j in range(len(matriz1[i])):
            #para poder acceder a los elementos de las matrices
            nuevo_numero = matriz1[i][j] + matriz2[i][j]
            nueva_fila.append(nuevo_numero)
        #se añade la fila con cada elemento sumado a la matriz creada
        matriz_aux.append(nueva_fila)

    return matriz_aux


# Ejercicio 2
def validar(grafo):
    #si no encontramos las claves nodos o aristas el grafo no será válido
    if "nodos" not in grafo: return False
    if "aristas" not in grafo: return False

    #en nodos guardaremos un conjunto de los nodos para tener un acceso rápido
    nodos = set(grafo["nodos"])
    #en aristas guardaremos el diccionario de todas las aristas de cada vértice
    aristas = grafo["aristas"]
    
    #comprobamos si los el conjunto de nodos coincide con el conjunto de las claves de las aristas
    nodos_aristas = set(aristas.keys())
    if nodos_aristas != nodos: return False

    for origen, destinos in aristas.items():
        for destino in destinos:
            #si para cada arista de un nodo va a un nodo inexistente en la lista de nodos no será válido
            if destino not in nodos: return False

        #como en los conjuntos se eliminan los duplicados confirmamos que no hay aristas repetidas
        if len(destinos) != len(set(destinos)): return False

    return True


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

matriz3 = [[1, 0, 1], 
           [0, 3, 2], 
           [1, 2, 2]
        ]

print(dimension(matriz1))
print(dimension(matriz2))

print('es cuadrada' if es_cuadrada(matriz1) else 'no es cuadrada')

a = multiplica_escalar(matriz1, 10)

print(a)

b = suma(matriz2, matriz3)

print(b)

g = {"nodos": ["a", "b", "c", "d"],
  "aristas": {"a": ["a", "b", "c"],
            "b": ["a", "c"],
            "c": ["c"],
            "d": ["c"]
            }
    }


if (validar(g)):print("grafo ok ")
