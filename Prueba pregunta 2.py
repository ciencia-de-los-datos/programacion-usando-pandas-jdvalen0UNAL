import pandas as pd

# Cargar el archivo tbl0.tsv desde la ubicación actual o el path que corresponda
tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    # Obtener la cantidad de columnas en tbl0
    cantidad_columnas = len(tbl0.columns)
    
    return cantidad_columnas

# Llamar a la función pregunta_02 para obtener la respuesta
respuesta = pregunta_02()

# Imprimir la respuesta
print(respuesta)



