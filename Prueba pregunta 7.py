import pandas as pd

def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    # Cargamos el archivo tbl0.tsv en un DataFrame
    df = pd.read_csv("tbl0.tsv", sep="\t")
    
    # Calculamos la suma de _c2 por cada letra en la columna _c1
    suma_por_letra = df.groupby('_c1')['_c2'].sum()
    
    # Retornamos el resultado
    return suma_por_letra

# Llamamos a la función y almacenamos el resultado en la variable 'resultado'
resultado = pregunta_07()

# Imprimimos el resultado
print(resultado)
