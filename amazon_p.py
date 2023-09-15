import pandas as pd


url = "up_amazon.xlsx"

df = pd.read_excel(url)

columnas_a_eliminar = ["category","discounted_price","discount_percentage","rating","rating_count","about_product","user_id","user_name","review_id","review_title","review_content","product_link"]

df = df.drop(columnas_a_eliminar, axis=1)

df.to_excel("Amazon_p.xlsx", index=False)

print("Actualizacion completa")