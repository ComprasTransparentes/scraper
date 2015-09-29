

/* RANKING DE CATEGORIAS EN LAS QUE SE GASTA MAS DINERO */
-- la cantidad lleva un case debido a errores en la fuente
SELECT XYZ.categoria,
	sum(XYZ.totalMonto)
FROM (
		SELECT Q.categoria,
			Q.itemQuant * Q.itemMontoUnit * QQ.tipo_cambio as totalMonto,
			cast(substring(S.fecha from 3 for 2) as integer) as month,
			cast(substring(S.fecha from 5 for 4) as integer) as year,
			MM.region_unidad as region
		FROM (
			SELECT A.id as itemId,
					CASE WHEN cast(B.cantidad as float) < cast(A.cantidad as float) THEN cast(B.cantidad  as float) ELSE cast(A.cantidad as float) END as itemQuant,
				cast(A.monto_unitario as float) as itemMontoUnit,
				A.company_id as companyId,
				B.tender_id as tenderId,
				B.categoria as categoria
			FROM adjudication_items A
			LEFT JOIN tender_items B
			on A.tender_item_id = B.id
			) Q
		INNER JOIN (
			SELECT 	tender_id as tenderId,
					date as fecha
			FROM tender_states
			WHERE state = '8'
		) S
		on Q.tenderId = S.tenderId
		LEFT JOIN tenders R
		on R.id = Q.tenderId
		LEFT JOIN currency QQ
		on QQ.moneda = R.moneda
		LEFT JOIN public_companies MM
		ON MM.id = Q.tenderId )XYZ
group by categoria
order by sum(XYZ.totalMonto) DESC
LIMT 15;



/* RANKING DE CATEGORIAS EN LAS QUE SE GASTA MAS DINERO POR REGION Y SEMESTRE */
-- la cantidad lleva un case debido a errores en la fuente

DROP TABLE IF EXISTS temp3;

CREATE TEMP TABLE temp3 AS
SELECT XYZ.categoria,
	sum(XYZ.totalMonto) as totalMonto,
	CASE WHEN month <= '6' AND year = '2013' THEN 'S1'
	WHEN month > '6' AND year = '2013' THEN 'S2'
	WHEN month <= '6' AND year = '2014' THEN 'S3'
	WHEN month > '6' AND year = '2014' THEN 'S4'
	WHEN month <= '6' AND year = '2015' THEN 'S5'
	ELSE 'S6' END as Semestre,
	region_unidad
FROM (
		SELECT Q.categoria,
			Q.itemQuant * Q.itemMontoUnit * QQ.tipo_cambio as totalMonto,
			cast(substring(S.fecha from 3 for 2) as integer) as month,
			cast(substring(S.fecha from 5 for 4) as integer) as year,
			MM.region_unidad as region_unidad
		FROM (
			SELECT A.id as itemId,
					CASE WHEN cast(B.cantidad as float) < cast(A.cantidad as float) THEN cast(B.cantidad  as float) ELSE cast(A.cantidad as float) END as itemQuant,
				cast(A.monto_unitario as float) as itemMontoUnit,
				A.company_id as companyId,
				B.tender_id as tenderId,
				B.categoria as categoria
			FROM adjudication_items A
			LEFT JOIN tender_items B
			on A.tender_item_id = B.id
			) Q
		INNER JOIN (
			SELECT 	tender_id as tenderId,
					date as fecha
			FROM tender_states
			WHERE state = '8'
		) S
		on Q.tenderId = S.tenderId
		LEFT JOIN tenders R
		on R.id = Q.tenderId
		LEFT JOIN currency QQ
		on QQ.moneda = R.moneda
		LEFT JOIN public_companies MM
		ON MM.id = Q.tenderId )XYZ
group by categoria, Semestre, region_unidad;

(select * from temp3 where semestre = 'S1' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Atacama ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Antofagasta ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Coquimbo ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región del Biobío ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de los Lagos ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Tarapacá  ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Magallanes y de la Antártica' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región Metropolitana de Santiago' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región Aysén del General Carlos Ibáñez del Campo' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Los Ríos' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de la Araucanía ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Arica y Parinacota' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región del Maule ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región del Libertador General Bernardo O´Higgins' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S1' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S2' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S3' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S4' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S5' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15)
union all
(select * from temp3 where semestre = 'S6' and region_unidad='Región de Valparaíso ' order by totalMonto DESC limit 15);

