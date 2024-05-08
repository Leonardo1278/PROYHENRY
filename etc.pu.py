import json
import pandas as pd

ruta = 'australian_user_reviews.json'
json_objects = []

with open(ruta, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            # Reemplazar comillas simples por dobles y luego convertir a objeto JSON
            corrected_line = line.replace("'", '"')
            json_object = json.loads(corrected_line)
            json_objects.append(json_object)
            print(json_object)  # Opcional: imprimir para verificar los objetos
        except json.JSONDecodeError as e:
            #print("Error al decodificar JSON en la línea:", line.encode('utf-8'))
            #print("Detalle del error:", str(e))
            pass

df_user_reviews = pd.DataFrame(json_objects)
print(df_user_reviews.head())

