import pandas as pd

def pregunta_05():
    # Leer el archivo tbl0.tsv
    df = pd.read_csv("tbl0.tsv", sep="\t")
    
    # Calcular el valor máximo de _c2 por cada letra en _c1
    resultado = df.groupby('_c1')['_c2'].max()
    
    return resultado

# Llamar a la función e imprimir el resultado
print(pregunta_05())
