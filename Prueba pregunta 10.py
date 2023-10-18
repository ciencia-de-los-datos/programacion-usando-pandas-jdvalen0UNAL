import pandas as pd

def pregunta_10():
    # Cargar el archivo tbl0.tsv
    df = pd.read_csv('tbl0.tsv', sep='\t')

    # Agrupar por _c1 y ordenar los valores de _c2
    grouped_df = df.groupby('_c1')['_c2'].apply(lambda x: ':'.join(map(str, sorted(x)))).reset_index()

    # Configurar _c0 como índice
    grouped_df.set_index('_c0', inplace=True)

    # Ordenar los índices
    grouped_df.sort_index(inplace=True)

    return grouped_df
# Llamar a la función
df_resultado = pregunta_10()

# Imprimir el DataFrame retornado
print("DataFrame resultante:")
print(df_resultado)











