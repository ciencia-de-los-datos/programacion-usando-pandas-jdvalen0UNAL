import pandas as pd

def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    # Cargamos el archivo tbl0.tsv en un DataFrame
    df = pd.read_csv("tbl0.tsv", sep="\t")
    
    # Agregamos una nueva columna llamada 'suma' que contiene la suma de '_c0' y '_c2'
    df['suma'] = df['_c0'] + df['_c2']
    
    # Retornamos el DataFrame resultante
    return df

# Llamamos a la función y almacenamos el resultado en la variable 'resultado'
resultado = pregunta_08()

# Imprimimos el resultado
print(resultado)
