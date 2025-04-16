--Creamos una tabla temporal para definir los parametros de la fecha base y de los "N", es decir, la duración minima de racha.
WITH parametros AS (
  SELECT 
    DATE('2024-02-01') AS fecha_base,
    3 AS n
),
-- Creamos otra tabla temporal para obtener los meses anteriores o iguales a la fecha base anterior.
-- Lo usamos para construir una especie de calendario por cleinte.
meses_disponibles AS (
  SELECT DISTINCT corte_mes
  FROM historia
  WHERE corte_mes <= (SELECT fecha_base FROM parametros)
),
-- Creamos una tercera tabla temporal, para unir las dos anteriores y así asegurar que todos los cientes
-- tengan datos en todos los meses.
clientes_meses AS (
  SELECT 
    c.cliente_id, 
    m.corte_mes
  FROM (SELECT DISTINCT cliente_id FROM historia) c
  CROSS JOIN meses_disponibles m
),
-- Unimos la tabla anterior con historia, para realizar una matriz, si no hay saldo la llenamos con valor 0.
-- Si el cliente no se ha retirado, le ponemos fecha ficticia del año 9999.
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
-- Clasificamos cada saldo mensual de los clientes en las categorías dadas.
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
-- En la columna grupo agrupamos filas consecutivas que tienen el mismo nivel y podemos comparar una racha potencial.
nivel_consecutivo AS (
  SELECT 
    cliente_id,
    corte_mes,
    nivel,
    ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY corte_mes) -
    ROW_NUMBER() OVER (PARTITION BY cliente_id, nivel ORDER BY corte_mes) AS grupo
  FROM niveles
),
-- Una vez realizada la agrupación en la tabla anteior, podemos contar cuantos meses consecutivos tuvo ese cliente la racha del nivel.
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
-- En esta tabla simplemente validamos y filtramos que la racha sea válida de acuerdo a los parámetros establecidos al inicio.
rachas_validas AS (
  SELECT *
  FROM rachas, parametros
  WHERE racha >= n
    AND fecha_fin <= fecha_base
),
-- De las rachas filtradas, escogemos la última más larga para cada cliente y si hay empate en rachas, nos quedamos con la última por DESC.
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
-- Acá en la consulta final, devolvemos ordenado como nos sugiere el ejercicio, viendo su racha más larga y reciente según los parámetros iniciales establecidos.
SELECT
  cliente_id AS identificacion,
  racha,
  fecha_fin,
  nivel
FROM racha_final
ORDER BY cliente_id;
