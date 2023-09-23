"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


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


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    # Obtener la cantidad de columnas en tbl0
    cantidad_columnas = len(tbl0.columns)
    
    return cantidad_columnas


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


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    """
    # Leer el archivo tbl0.tsv en un DataFrame llamado tbl0
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

    # Agrupar los datos por la columna '_c1' y calcular el promedio de '_c2'
    resultado = tbl0.groupby('_c1')['_c2'].mean()

    # Devolver el resultado como un DataFrame sin incluir el nombre de la columna '_c1'
    return resultado.rename_axis(None)

def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    # Leer el archivo tbl0.tsv
    df = pd.read_csv("tbl0.tsv", sep="\t")
    
    # Calcular el valor máximo de _c2 por cada letra en _c1
    resultado = df.groupby('_c1')['_c2'].max()
    
    return resultado


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
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
    # Cargar el archivo tbl0.tsv en un DataFrame
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Agregar la columna "year" al DataFrame
    df['year'] = pd.to_datetime(df['_c3']).dt.year

    # Reemplazar NaN por 0 en la columna "year" y convertirla a enteros
    df['year'] = df['year'].fillna(0).astype(int)

    # Devolver el DataFrame resultante sin mostrar índices
    return df



def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    return


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    return


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    return


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    return
