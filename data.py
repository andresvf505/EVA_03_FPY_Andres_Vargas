'''este algoritmo administra una tienda de pinturas'''

from pathlib import Path
import json
import csv
import os

lista = ['Ver lista de pintura',
         'Buscar pintura',
         'Agregar pintura',
         'Eliminar pintura',
         'Exportar pintura']
home = Path(__file__).parent
ruta_p = Path(home/'archivo.json')




def pantalla():
    os.system('cls')

def listar(lista):
    while True:
        for ind, opt in enumerate(lista):
            print(f'{ind + 1},{opt}')
            break

def inventario(r):
    with open(r,mode='r')as stream:
        json.load(stream)

def crear_file():
    Path('archivo.json').touch

def resp():
    resp = input('¿que quieres hacer?')
    return resp







