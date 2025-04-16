import sqlite3
import pandas as pd

# Este archivo fue creado especialmente para verificar dos cosas:
# 1. Que la conexión establecida en el archivo setup_database.py estuviera bien formulada.
# 2. Poder verificar el schema o estructura de la tabla referenciada.
conn = sqlite3.connect('database_tuya.db')
print("Columnas de:")
print(pd.read_sql_query("PRAGMA table_info(clientes);", conn))
conn.close()
