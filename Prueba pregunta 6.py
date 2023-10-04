import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 del archivo `tbl1.tsv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    """
    # Cargamos el archivo tbl1.tsv en un DataFrame
    df = pd.read_csv("tbl1.tsv", sep="\t")
    
    # Obtenemos los valores únicos de la columna _c4, los convertimos a mayúsculas y los ordenamos
    valores_unicos = df['_c4'].unique()
    valores_unicos = [valor.upper() for valor in valores_unicos]
    valores_unicos.sort()
    
    # Retornamos el resultado
    return valores_unicos

# Llama a la función para obtener la lista de valores únicos
resultado = pregunta_06()

# Imprime el resultado aparte
print(resultado)
