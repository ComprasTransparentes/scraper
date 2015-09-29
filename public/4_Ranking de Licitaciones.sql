/* RANKING NACIONAL DE LICITACIONES  */

-- para obtener los resultados a nivel de ventana temporal, es necesario filtrar
-- mediante un where
SELECT MA.tenderCode,
	MA.totalMonto
FROM (
	SELECT 	Q.tenderId as tenderId,
		Q.itemQuant * QQ.tipo_cambio as totalMonto,
		R.code as tenderCode,
		cast(substring(S.fecha from 1 for 2) as integer) as day,
		cast(substring(S.fecha from 3 for 2) as integer) as month,
		cast(substring(S.fecha from 5 for 4) as integer) as year,
		MM.code,
		MM.nombre,
		MM.codigo_unidad,
		MM.nombre_unidad,
		MM.comuna_unidad,
		MM.region_unidad
	FROM (
		SELECT sum(cast(A.cantidad as float) * cast(A.monto_unitario as float)) as itemQuant,
			B.tender_id as tenderId
		FROM adjudication_items A
		LEFT JOIN tender_items B
		on A.tender_item_id = B.id
		GROUP by B.tender_id
		) Q
	LEFT JOIN tenders R
	ON R.id = Q.tenderId
	INNER JOIN (
		SELECT tender_id as tenderId,
			date as fecha
		FROM tender_states
		WHERE state = '8'
		) S
	ON Q.tenderId = S.tenderId
	LEFT JOIN public_companies MM
	ON MM.id = Q.tenderId
	LEFT JOIN currency QQ
	on QQ.moneda = R.moneda
	) MA
ORDER BY MA.totalMonto DESC
LIMIT 15;
/*WHERE dia = '10' */

/* RANKING DE LICITACIONES A NIVEL DE REGION */

-- para obtener los resultados a nivel de ventana temporal, es necesario filtrar
-- mediante un where


DROP TABLE IF EXISTS temp2;
CREATE TEMP TABLE temp2 AS
SELECT MA.tenderCode,
	CASE 	WHEN month <= '6' AND year = '2013' THEN 'S1'
		WHEN month > '6' AND year = '2013' THEN 'S2'
		WHEN month <= '6' AND year = '2014' THEN 'S3'
		WHEN month > '6' AND year = '2014' THEN 'S4'
		WHEN month <= '6' AND year = '2015' THEN 'S5'
		ELSE 'S6' END as Semestre,
	MA.totalMonto,
	MA.region_unidad
FROM (
	SELECT 	Q.tenderId as tenderId,
		Q.itemQuant * QQ.tipo_cambio as totalMonto,
		R.code as tenderCode,
		cast(substring(S.fecha from 1 for 2) as integer) as day,
		cast(substring(S.fecha from 3 for 2) as integer) as month,
		cast(substring(S.fecha from 5 for 4) as integer) as year,
		MM.code,
		MM.nombre,
		MM.codigo_unidad,
		MM.nombre_unidad,
		MM.comuna_unidad,
		MM.region_unidad
	FROM (
		SELECT sum(cast(A.cantidad as float) * cast(A.monto_unitario as float)) as itemQuant,
			B.tender_id as tenderId
		FROM adjudication_items A
		LEFT JOIN tender_items B
		on A.tender_item_id = B.id
		GROUP by B.tender_id
		) Q
	LEFT JOIN tenders R
	ON R.id = Q.tenderId
	INNER JOIN (
		SELECT tender_id as tenderId,
			date as fecha
		FROM tender_states
		WHERE state = '8'
		) S
	ON Q.tenderId = S.tenderId
	LEFT JOIN public_companies MM
	ON MM.id = R.buyer_id
	LEFT JOIN currency QQ
	on QQ.moneda = R.moneda
	) MA
ORDER BY  MA.region_unidad,MA.totalMonto DESC;

(select * from temp2 where semestre = 'S1' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S1' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S2' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S3' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S4' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S5' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp2 where semestre = 'S6' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15);
