
--Primero creamos una ventana o tabla temporal, para poder buscar la categória más fecuente
WITH ranked_categorias AS (
    SELECT
        t.cliente_id,
        cc.departamento,
        cc.nombre_categoria,
        COUNT(*) AS total_transacciones,
        MAX(t.fecha_transaccion) AS ultima_fecha,
        --Contamos el número de transacciones y sacamos la última fecha de esa transacci´´on.
        ROW_NUMBER() OVER (
            PARTITION BY t.cliente_id, cc.departamento
            ORDER BY COUNT(*) DESC, MAX(t.fecha_transaccion) DESC
        ) AS ranking
        --GEneramos un número de orden para cada cliente y departamento, ordenado por las transacciones yla fecha más reciente.
    FROM transacciones t
    JOIN categorias_consumo cc 
        ON t.codigo_categoria = cc.codigo_categoria
    WHERE t.estado = 'Aprobada'
    AND t.fecha_transaccion BETWEEN '2023-01-01' AND '2024-01-01'  
    GROUP BY t.cliente_id, cc.departamento, cc.nombre_categoria
)
--Filtramos sólo las transacciones aprobadas y las que estén dentro del rango dado
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
-- En la consulta final, llamamos los campos creados en la tabla temporal y la unimos con cleintes
-- filtramos para quedarnos con los que tienen la categoría dada (mayor frecuencia si es 1), 
-- heredando las condiciones de la fecha otorgada en la tabla anterior.