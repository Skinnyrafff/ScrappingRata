import requests
from bs4 import BeautifulSoup
import sys

# Configura la codificación de salida estándar a UTF-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://descuentosrata.com/guata"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    productos = soup.find_all('div',class_="my-2 col-md-6 col-lg-4 col-12")
    print("Productos encontrados:",len(productos))

    for producto in productos:
            titulo = producto.find('h6', class_="mb-1 text-muted")
            descuento = producto.find('span',class_="mr-1 text-dark d-block-inline")
            detalles = producto.find('span',class_="text-dark")
            disponibilidad = producto.find('span',class_="guata-disp")
        
            if titulo:
                print("Titulo:",titulo.text.strip())
                print("Descuento:",descuento.text.strip())
                print("Detalles:",detalles.text.strip())
                print("Disponibilidad:",disponibilidad.text.strip())
                
                
                print("\n")



else:
    print ("Error al cargar la web, codigo:",response.status_code)