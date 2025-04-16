import sqlite3
import pandas as pd
#Este archivo fue creado con la intención de verificar la consulta SQL ejecutada en el archivo ejercicio3.sql
# Llamamos la conexión BD
conn = sqlite3.connect('database_tuya.db')

query = """
WITH parametros AS (
  SELECT 
    DATE('2024-02-01') AS fecha_base,
    3 AS n
),
meses_disponibles AS (
  SELECT DISTINCT corte_mes
  FROM historia
  WHERE corte_mes <= (SELECT fecha_base FROM parametros)
),
clientes_meses AS (
  SELECT 
    c.cliente_id, 
    m.corte_mes
  FROM (SELECT DISTINCT cliente_id FROM historia) c
  CROSS JOIN meses_disponibles m
),
saldos_completos AS (
  SELECT
    cm.cliente_id,
    cm.corte_mes,
    COALESCE(h.saldo, 0) AS saldo,
    r.fecha_retiro
  FROM clientes_meses cm
  LEFT JOIN historia h 
    ON cm.cliente_id = h.cliente_id AND cm.corte_mes = h.corte_mes
  LEFT JOIN retiros r 
    ON cm.cliente_id = r.cliente_id
  WHERE cm.corte_mes <= IFNULL(r.fecha_retiro, DATE('9999-12-31'))
),
niveles AS (
  SELECT
    cliente_id,
    corte_mes,
    saldo,
    CASE
      WHEN saldo < 300000 THEN 'N0'
      WHEN saldo < 1000000 THEN 'N1'
      WHEN saldo < 3000000 THEN 'N2'
      WHEN saldo < 5000000 THEN 'N3'
      ELSE 'N4'
    END AS nivel
  FROM saldos_completos
),
nivel_consecutivo AS (
  SELECT 
    cliente_id,
    corte_mes,
    nivel,
    ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY corte_mes) -
    ROW_NUMBER() OVER (PARTITION BY cliente_id, nivel ORDER BY corte_mes) AS grupo
  FROM niveles
),
rachas AS (
  SELECT
    cliente_id,
    nivel,
    MIN(corte_mes) AS fecha_inicio,
    MAX(corte_mes) AS fecha_fin,
    COUNT(*) AS racha
  FROM nivel_consecutivo
  GROUP BY cliente_id, nivel, grupo
),
rachas_validas AS (
  SELECT *
  FROM rachas, parametros
  WHERE racha >= n
    AND fecha_fin <= fecha_base
),
racha_final AS (
  SELECT *
  FROM (
    SELECT *,
      ROW_NUMBER() OVER (
        PARTITION BY cliente_id 
        ORDER BY racha DESC, fecha_fin DESC
      ) AS rn
    FROM rachas_validas
  )
  WHERE rn = 1
)

SELECT
  cliente_id AS identificacion,
  racha,
  fecha_fin,
  nivel
FROM racha_final
ORDER BY cliente_id;
"""
df_resultado = pd.read_sql_query(query, conn)

# Como una validación más obtenemos el total de los diferentes clientes
total_clientes = pd.read_sql_query("SELECT COUNT(DISTINCT cliente_id) AS total FROM historia", conn).iloc[0, 0]
conn.close()

# Adicional a los requerimientos podemos visualizar la cantidad total de los clientes y de esos los que cumplieron
# con la condición inicial de la racha, dada al inicio.
print(df_resultado)
print(f"\nDel total de {total_clientes} clientes, {df_resultado.shape[0]} cumplieron con la racha.\n")
