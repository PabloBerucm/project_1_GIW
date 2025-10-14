"""
TODO: rellenar

Asignatura: GIW
Práctica 4
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""

import sqlite3
import csv
from datetime import datetime


def crear_bd(db_filename):
    # Conecta o crea la base de datos
    con = sqlite3.connect(db_filename)
    cur = con.cursor()

    # Borra las tablas si ya existen
    cur.execute("DROP TABLE IF EXISTS semanales_IBEX35")
    cur.execute("DROP TABLE IF EXISTS datos_generales")

    # Crea la tabla datos_generales
    cur.execute("""
        CREATE TABLE datos_generales (
            ticker TEXT PRIMARY KEY,
            nombre TEXT,
            indice TEXT,
            pais TEXT
        )
    """)

    # Crea la tabla semanales_IBEX35
    cur.execute("""
        CREATE TABLE semanales_IBEX35 (
            ticker TEXT,
            fecha TEXT,
            precio REAL,
            PRIMARY KEY (ticker, fecha),
            FOREIGN KEY (ticker) REFERENCES datos_generales(ticker)
        )
    """)

    con.commit()
    con.close()


def cargar_bd(db_filename, tab_datos, tab_ibex35):
    con = sqlite3.connect(db_filename)
    cur = con.cursor()

    # Cargar datos_generales
    with open(tab_datos, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            cur.execute("INSERT INTO datos_generales VALUES (?, ?, ?, ?)",
                        (fila["ticker"], fila["nombre"], fila["indice"], fila["pais"]))

    # Cargar semanales_IBEX35
    with open(tab_ibex35, "r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            # Cambiar formato de fecha de DD/MM/YYYY HH:MM a YYYY-MM-DD HH:MM
            fecha_original = fila["fecha"]
            fecha_nueva = datetime.strptime(fecha_original, "%d/%m/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
            cur.execute("INSERT INTO semanales_IBEX35 VALUES (?, ?, ?)",
                        (fila["ticker"], fecha_nueva, float(fila["precio"])))

    con.commit()
    con.close()



def consulta1(db_filename, indice):
    con = sqlite3.connect(db_filename)
    cur = con.cursor()

    cur.execute('''
        SELECT ticker, nombre
        FROM datos_generales
        WHERE indice LIKE ?
        ORDER BY ticker ASC
        ''', (indice,)
    )    
    sol = cur.fetchall()
    con.close()
    return sol


def consulta2(db_filename):
    ...


def consulta3(db_filename, limite):
    ...


def consulta4(db_filename, ticker):
    ...


crear_bd('bolsa.sqlite3')
cargar_bd(
    'bolsa.sqlite3',
    'D:/AA_DatosUsb/AA_SegundoUSB/GIW/Practica_4/Tabla1.csv',
    'D:/AA_DatosUsb/AA_SegundoUSB/GIW/Practica_4/Tabla2.csv'
)
print(consulta1('bolsa.sqlite3', "Nasdaq 100"))
