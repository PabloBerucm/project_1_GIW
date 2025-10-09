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
    def __init__(self):
        self.texto = ""
        self.en_name = False
        self.nombres = set()

    def startElement(self, name, attrs):
        if name == "name":
            self.en_name = True
        self.texto = ""

    def characters(self, content):
        if self.en_name:
            self.texto += content

    def endElement(self, name):
        if name == "name":
            nombre = html.unescape(self.texto.strip())
            if nombre:
                self.nombres.add(nombre)
            self.en_name = False





def nombres_restaurantes(filename):
    h = ManejoRestaurantes()
    parser = xml.sax.make_parser()
    parser.setContentHandler(h)
    parser.parse(filename)

    return sorted(h.nombres)

def subcategorias(filename):
    ...


def info_restaurante(filename, name):
    ...


def busqueda_cercania(filename, lugar, n):
    ...

lista = nombres_restaurantes("Practica_3/restaurantes_v1_es_pretty.xml")
print(lista)