"""
TODO: rellenar

Asignatura: GIW
Práctica 5
Grupo: 3
Autores: Pablo Bernal Calleja
         Fernando Guzmán Muñoz
         Álvaro González-Barros Medina
         Guillermo Guzmán González Ortíz
         Nicolás López-Chaves Pérez 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""

import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

URL = 'https://books.toscrape.com/'


# APARTADO 1 #
def explora_categoria(url):
    """
    Devuelve una tupla (nombre, número de libros) explorando la URL de una categoría.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Obtener el nombre de la categoría desde el título de la página
        title = soup.find('h1').text.strip()
        
        # Obtener el número total de libros (si está disponible en el texto)
        article = soup.find('article', class_='product_pod')
        if article:
            pagination = soup.select_one('form .form-horizontal + ul.pager li.current')
            if pagination:
                text = pagination.text.strip()
                match = re.search(r'of (\d+)', text)
                if match:
                    total_pages = int(match.group(1))
                    num_books = total_pages * 20  # Asumiendo 20 libros por página
                else:
                    num_books = 20  # Si no hay paginación, asumimos 20 libros
            else:
                num_books = 20  # Valor por defecto si no hay paginación
        else:
            num_books = 0  # Si no hay productos, 0 libros
        
        return (title, num_books)
    except requests.RequestException:
        return ("Error", 0)


def categorias():
    """
    Devuelve un conjunto de parejas (nombre, número libros) de todas las categorías.
    """
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar la lista de categorías en la barra lateral
        sidebar = soup.find('div', class_='side_categories')
        categories = set()
        
        if sidebar:
            # Extraer enlaces de categorías
            for a in sidebar.find_all('a', href=True):
                category_url = urljoin(URL, a['href'])
                name, num_books = explora_categoria(category_url)
                categories.add((name, num_books))
        
        return categories
    except requests.RequestException:
        return set()


# APARTADO 2 #
def libros_categoria(nombre):
    """ Dado el nombre de una categoría, devuelve un conjunto de tuplas 
        (titulo, precio, valoracion), donde el precio será un número real y la 
        valoración un número natural """
    