import pandas as pd
import requests
from bs4 import BeautifulSoup

# Link de la pagina web que usarás
web = 'https://www.cronista.com/MercadosOnline/dolar.html'

# Realiza la solicitud HTTP y obtiene el contenido de la página
response = requests.get(web)
soup = BeautifulSoup(response.text, 'html.parser')
div_element = soup.find('div', class_='sell-value')
numero = div_element.get_text(strip=True).replace('$', '')
partes = numero.split(',')
numero_sin_decimales = partes[0]
num = int(numero_sin_decimales)

# Lee el archivo que se usara
df = pd.read_excel("Amazon_p.xlsx")

# Crea un nuevo DataFrame con la fila que deseas agregar
# nueva_fila = {'dolar': num}
# nuevo_df = pd.DataFrame([nueva_fila])

# Concatena el nuevo DataFrame con el DataFrame existente
# df = pd.concat([df, nuevo_df], ignore_index=True)

# Actualiza el valor de la fila 1468 con el nuevo valor de 'num'
df.loc[1468, 'dolar'] = num

# Mueve el valor anterior de la fila 1468 a la fila 1467
valor_anterior = df.loc[1468, 'dolar']
df.loc[1467, 'dolar'] = valor_anterior

# # Calcular el porcentaje de cambio en el valor del dólar
porcentaje_cambio_dolar = ((num - valor_anterior) / valor_anterior) * 100

print("Dólar anterior:", valor_anterior)
print("Dólar actual:", num)
# print("Porcentaje de cambio en el valor del dólar:", porcentaje_cambio_dolar)

# Actualizar los precios de acuerdo al porcentaje de cambio en el valor del dólar
df['actual_price'] = df['actual_price'] * (1 + porcentaje_cambio_dolar / 100)


# Guarda el DataFrame actualizado en el mismo archivo Excel
df.to_excel("Amazon_p.xlsx", index=False)


