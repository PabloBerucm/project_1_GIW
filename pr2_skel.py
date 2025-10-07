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
    ...

def dias_mas_accidentes(datos):
    ...

def puntos_negros_distrito(datos, distrito, k):
    ...


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
lista_accidentes = lee_fichero_accidentes("D:/AA_DatosUsb/AA_SegundoUSB/GIW/Practica_2/AccidentesBicicletas_2021.csv")
#compruebo la primera lectura del fichero imprimiendo la línea 0
print(lista_accidentes[0])
