import pandas as pd

def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    # Cargar el archivo tbl0.tsv
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Crear la nueva columna 'year'
    df['year'] = df['_c3'].str.split('-').str[0]

    return df

# Llamar a la función
df_resultado = pregunta_09()

# Imprimir el DataFrame retornado
print("DataFrame con la nueva columna 'year':")
print(df_resultado)