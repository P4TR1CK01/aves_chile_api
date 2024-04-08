'''//////////////////////////////////////////////
Descripción La asociación de Amantes de los pájaros de Chile ha notado que actualmente 
no se tiene información de los distintos pájaros que pueden ser observados en Chile. 
Es por eso que les gustaría poder entender a manera de prototipo como poder listar muchos de estos especímenes. 
Para ello se le solicita generar un prototipo muy sencillo en el cual se puedan observar algunas 
imágenes de pájaros típicos de Chile junto con su nombre en español e inglés. La idea es que esta información 
pueda ser eventualmente transformada en señaléticas bilingües que permitan fomentar el turismo en Chile.  
Para ello se le da acceso a la API  'https://aves.ninjas.cl/api/birds', 
la cual da acceso a una base de datos con la información requerida. Se solicita entonces que usted pueda crear 
un script en Python que permita crear este sitio web con los requerimientos solicitados, es decir, 
un listado con el título Aves de Chile, y cada especie registrada con su nombre en inglés y español junto con sus imágenes. 
No olvide que a pesar de que el requerimiento es sencillo, debemos respetar las buenas prácticas de modularización. 
//////////////////////////////////////////////'''
# Importamos librerias y funciones a utilizar
import requests
import json
from html_maker import make_cols3, make_full_html

# Solicito las imagenes
photos = requests.get('https://aves.ninjas.cl/api/birds')                     

# Transformo el resultado a una lista json
photos = photos.json()

# Definimos la cantidad de items en la lista 
photo = photos[:100]

# Armamos el texto que contiene  la descripción y nombre del ave
cols_3 = make_cols3(photos)

# Armamos el HTML completo
html_completo = make_full_html(cols_3)

# Crear una funcion para crear el archivo HTML 
def  crear_html():
  with open('output.html', 'w', encoding = 'utf-8') as file:
    return file.write(html_completo)
crear_html()