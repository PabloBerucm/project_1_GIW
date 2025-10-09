"""
TODO: rellenar

Asignatura: GIW
Práctica 3
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""

import xml.sax
import html

class ManejoRestaurantes(xml.sax.ContentHandler):
    """
    Creamos una clase contenthandler cuyo constructor tendrá 3 atributos, el texto para almacenar
    lo leído por invocaciones consecutivas, el en_name para saber si estamos en el atributo name y
    coger el nombre y un conjunto nombres donde iremos guardando los nombres de restaurantes
    """
    def __init__(self):
        self.texto = ""
        self.en_name = False
        self.nombres = set()

    def startElement(self, name, attrs):
        #cuando detecta la etiqueta element se pone en true nuestro en_name
        if name == "name":
            self.en_name = True
        #borramos lo que hubiese leído en el registro para coger solo el nombre
        self.texto = ""

    def characters(self, content):
        #cuando está leyendo el contenido de la etiqueta y nos encontramos en en_name, y lo guardamos en el texto
        if self.en_name:
            self.texto += content

    def endElement(self, name):
        #cuando terminamos de ver un elemento si la etiqueta era name:
        if name == "name":
            #usamos el html.unescape() por el texto escapado html y el strip para eliminar espacios al principio y al final
            nombre = html.unescape(self.texto.strip())
            #si existe el nombre lo añadimos a nuestro conjunto
            if nombre:
                self.nombres.add(nombre)
            #y como terminamos la etiqueta de name ponemos la flag a False
            self.en_name = False





def nombres_restaurantes(filename):
    h = ManejoRestaurantes()
    parser = xml.sax.make_parser()
    parser.setContentHandler(h)
    parser.parse(filename)
    #usamos el método sorted para transformar el conjunto en una lista ordenada
    return sorted(h.nombres)

def subcategorias(filename):
    ...


def info_restaurante(filename, name):
    ...


def busqueda_cercania(filename, lugar, n):
    ...

lista = nombres_restaurantes("Practica_3/restaurantes_v1_es_pretty.xml")
print(lista)
