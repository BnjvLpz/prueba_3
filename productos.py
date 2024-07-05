import globales
import os
import json
import random



productos = [
"Café Americano",
"Té Chai",
"Croissant",
"Jugo Naranja",
"Panini de Pavo y Queso",
"Pastel de Zanahoria",
"Espresso Doble",
"Ba;do de Frutas",
"Muffin",
"Ensalada",
"Chocolate Caliente",
"Tarta de Frambuesa",
"Sándwich de Huevo",
"Galletas de Avena",
"Frappé de Caramelo"
]


def ventas_alea():
    for productos in productos:
        for valor in productos:
            valor = random.choice(2000, 10000) * 100
            globales.guardar_archivo_json("productos.json")