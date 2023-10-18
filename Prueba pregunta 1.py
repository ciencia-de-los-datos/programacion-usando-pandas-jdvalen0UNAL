import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    # Utiliza el método shape para obtener el número de filas
    cantidad_filas = tbl0.shape[0]
    
    # Retorna la cantidad de filas como un entero
    return cantidad_filas

# Llama a la función pregunta_01 y almacena la respuesta en una variable
respuesta_01 = pregunta_01()

# Imprime la respuesta
print(respuesta_01)
