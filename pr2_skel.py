"""
TODO: rellenar

Asignatura: GIW
Práctica 2
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""


### Formato CSV
import csv
def lee_fichero_accidentes(ruta):
    #vamos a leer el fichero usando csv.DictReader para que nos devuelva
    #un diccionario por cada fila y poder acceder a cada elemento por clave

    #como necesitamos devolver una lista de diccionarios crearemos una lista
    #a la que iremos añadiendo las líneas leídas como diccionarios en el fichero

    lista_accidentes = []

    with open(ruta, 'r', newline='', encoding='utf8') as fich:
        #aquí como el delimitador correcto es ; y no , que es el predeterminado de csv hay que cambiarlo con delimiter
        lector = csv.DictReader(fich, delimiter=';')
        for linea in lector:
            lista_accidentes.append(linea)
    return lista_accidentes

def accidentes_por_distrito_tipo(datos):
    #función que devuelve un diccionario pasando el de lee_fichero_accidentes
    #devolviendo otro diccionario que contée los accidentes por distrito
    dicc_sol = {}

    for item in datos:
        #estandarizamos el texto a la salida buscada por el ejercicio
        distrito = item['distrito'].strip().upper()
        tipo = item['tipo_accidente'].strip()

        clave = (distrito, tipo)

        #si ya existe la clave en nuestro diccionario añadiremos un accidente
        #como valor, de lo contrario, lo añadiremos al diccionario con un 1
        if clave in dicc_sol:
            dicc_sol[clave] += 1
        else:
            dicc_sol[clave] = 1
    #devolveremos el diccionario generado
    return dicc_sol

def dias_mas_accidentes(datos):
    dicc_fechas = {}

    for item in datos:
        fecha = item['fecha'].strip()
        dicc_fechas[fecha] = dicc_fechas.get(fecha, 0) + 1

    # máximo número de accidentes en un día
    max_acc = max(dicc_fechas.values())

    # devolvemos todas las fechas con ese número de accidentes
    dias_maximos = [fecha for fecha, n in dicc_fechas.items() if n == max_acc]

    return dias_maximos

def puntos_negros_distrito(datos, distrito, k):
    distrito = distrito.strip().upper()
    conteo = {}

    for item in datos:
        if item['distrito'].strip().upper() == distrito:
            punto = item.get('localizacion', item.get('direccion', '')).strip()
            conteo[punto] = conteo.get(punto, 0) + 1

    # ordenamos los puntos por número de accidentes (descendente)
    puntos_ordenados = sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    # devolvemos los k primeros puntos
    return puntos_ordenados[:k]


#### Formato JSON
def leer_monumentos(ruta):
    ...

def codigos_postales(monumentos):
    ...

def busqueda_palabras_clave(monumentos, palabras):
    ...

def busqueda_distancia(monumentos, direccion, distancia):
    ...


#pruebas del código

#leer fichero csv -> indicar ruta propia del fichero csv para su lectura
mi_lista_accidentes = lee_fichero_accidentes("D:/AA_DatosUsb/AA_SegundoUSB/GIW/Practica_2/AccidentesBicicletas_2021.csv")
#compruebo la primera lectura del fichero imprimiendo la línea 0
print(mi_lista_accidentes[0])

#comprobamos la segunda función
accidentes_distrito_tipo = accidentes_por_distrito_tipo(mi_lista_accidentes)
print(accidentes_distrito_tipo)

print(dias_mas_accidentes(mi_lista_accidentes))
print(puntos_negros_distrito(mi_lista_accidentes, "CENTRO", 5))
