import sqlite3
import pandas as pd

#leemos los archivos excel en cada uno de los archivos y los sepraramos según su hoja del archivo excel
clientes_df= pd.read_excel('../data/bd.xlsx', sheet_name='CLIENTES')
transacciones_df= pd.read_excel('../data/bd.xlsx', sheet_name='TRANSACCIONES')
categorias_consumo_df= pd.read_excel('../data/bd.xlsx', sheet_name='CATEGORIAS_CONSUMO')
historia_df = pd.read_excel('../data/rachas.xlsx', sheet_name='historia')
retiros_df = pd.read_excel('../data/rachas.xlsx', sheet_name='retiros')

#ponemos todos los nombres de las columnas en minisculas y quitamos espacios para estándarizar los nombres de las columnas
clientes_df.columns = clientes_df.columns.str.strip().str.lower()
transacciones_df.columns = transacciones_df.columns.str.strip().str.lower()
categorias_consumo_df.columns = categorias_consumo_df.columns.str.strip().str.lower()
historia_df.columns = historia_df.columns.str.strip().str.lower()
retiros_df.columns = retiros_df.columns.str.strip().str.lower()

#Acá renombramos las columnas con nombre diferente, es decir, igualamos el contenido del excel con el nombre en la creación de la BD
clientes_df.rename(columns={
    'identificación': 'cliente_id',
    'tipo tarjeta':'tipo_tarjeta',
    'feçha_apertura_tarjeta':'fecha_apertura_tarjeta',},inplace=True)
transacciones_df.rename(columns={
    'identificacion': 'cliente_id',},inplace=True)
historia_df.rename(columns={
    'identificacion': 'cliente_id',},inplace=True)
retiros_df.rename(columns={
    'identificacion': 'cliente_id',},inplace=True)

#Acá definimos la función para crear la BD, con los tipos de datos adecuados y cuidando las reestricciones
def create_database():
    conn = sqlite3.connect('database_tuya.db')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
        nombre TEXT,
        cliente_id TEXT PRIMARY KEY,
        tipo_documento TEXT,
        clasificacion TEXT CHECK (clasificacion IN ('Personal', 'Empresarial')),
        tipo_tarjeta TEXT CHECK (tipo_tarjeta IN ('Crédito', 'Débito')),
        fecha_apertura_tarjeta DATE,
        estado_tarjeta TEXT CHECK (estado_tarjeta IN ('Activa', 'Inactiva')))'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS transacciones (
        cliente_id TEXT,
        id_transaccion INTEGER,
        fecha_transaccion DATE,
        codigo_categoria INTEGER,
        estado TEXT CHECK (estado IN ('Aprobada', 'Rechazada')),
        valor_compra NUMERIC)''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS categorias_consumo (
        codigo_categoria INTEGER PRIMARY KEY,
        nombre_categoria TEXT,
        ciudad TEXT,
        departamento TEXT)'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS historia (
        cliente_id TEXT PRIMARY KEY,
        corte_mes DATE,
        saldo NUMERIC)'''
    )

    conn.execute('''
        CREATE TABLE IF NOT EXISTS retiros (
        cliente_id TEXT PRIMARY KEY,
        fecha_retiro DATE)'''
    )

    # Insertamos los datos en las tablas anteriormente creadas
    clientes_df.to_sql('clientes', conn, if_exists='replace', index=False)
    transacciones_df.to_sql('transacciones', conn, if_exists='replace', index=False)
    categorias_consumo_df.to_sql('categorias_consumo', conn, if_exists='replace', index=False)
    historia_df.to_sql('historia', conn, if_exists='replace', index=False)
    retiros_df.to_sql('retiros', conn, if_exists='replace', index=False)

    conn.close()

if __name__ == '__main__':
    create_database()



