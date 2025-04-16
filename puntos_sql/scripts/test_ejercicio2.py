import sqlite3
import pandas as pd

#Este archivo fue creado para verificar el resultado de la consulta SQL, visualizada en el archivo ejercicio2.sql
# Llamamos la conexión a la base de datos
conn = sqlite3.connect('database_tuya.db')

# Consulta SQL
query = """
WITH ranked_categorias AS (
    SELECT
        t.cliente_id,
        cc.departamento,
        cc.nombre_categoria,
        COUNT(*) AS total_transacciones,
        MAX(t.fecha_transaccion) AS ultima_fecha,
        ROW_NUMBER() OVER (
            PARTITION BY t.cliente_id, cc.departamento
            ORDER BY COUNT(*) DESC, MAX(t.fecha_transaccion) DESC
        ) AS ranking
    FROM transacciones t
    JOIN categorias_consumo cc 
        ON t.codigo_categoria = cc.codigo_categoria
    WHERE t.estado = 'Aprobada'
    AND t.fecha_transaccion BETWEEN '2023-01-01' AND '2024-01-01'  
    GROUP BY t.cliente_id, cc.departamento, cc.nombre_categoria
)

SELECT
    c.cliente_id,
    c.nombre,
    rc.departamento,
    rc.nombre_categoria AS categoria_preferida,
    rc.total_transacciones,
    rc.ultima_fecha
FROM ranked_categorias rc
JOIN clientes c ON rc.cliente_id = c.cliente_id
WHERE rc.ranking = 1
ORDER BY c.cliente_id, rc.departamento;
"""

# Ejecutamos y traemos los resultados
df_resultado = pd.read_sql_query(query, conn)
conn.close()
print(df_resultado)
