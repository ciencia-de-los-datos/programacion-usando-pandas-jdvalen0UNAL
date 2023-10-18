import pandas as pd

# Cargar los DataFrames desde los archivos
tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

# Pregunta 3
def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    cantidad_por_letra = tbl0['_c1'].value_counts()  # Contar la cantidad de registros por cada letra en la columna _c1
    cantidad_por_letra = cantidad_por_letra.sort_index()  # Ordenar el resultado por letras en orden alfabético
    cantidad_por_letra.index.name = None  # Eliminar el nombre del índice
    return cantidad_por_letra

# Llamar a la función pregunta_03 para obtener la respuesta
respuesta_03 = pregunta_03()

# Imprimir la respuesta
print(respuesta_03)




