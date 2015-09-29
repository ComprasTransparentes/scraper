/* QUERY PARA EL INICIO */

--genero una tabla sobre la cual calculo las metricas
DROP TABLE IF EXISTS temp4;

CREATE TABLE temp4 AS
SELECT Q.categoria,
	Q.itemQuant * Q.itemMontoUnit * QQ.tipo_cambio as totalMonto,
	cast(substring(S.fecha from 3 for 2) as integer) as month,
	cast(substring(S.fecha from 5 for 4) as integer) as year,
	MM.region_unidad as region_unidad,
	XY.name as ministerio
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
ON MM.id = Q.tenderId
INNER JOIN public_hierarchy XY
on MM.code = XY.company_code;

-- DATO 1: Monto total transado agrupado por año

SELECT sum(XYZ.totalMonto) as totalMonto,
	CASE WHEN year = '2013' THEN 'Y1'
	WHEN year = '2014' THEN 'Y2'
	ELSE 'Y3' END as Semestre
FROM temp4 XYZ
group by Semestre;

-- DATO 2: Licitaciones adjudicadas por año

SELECT count(AA.*),
	CASE WHEN year = '2013' THEN 'Y1'
	WHEN year = '2014' THEN 'Y2'
	ELSE 'Y3' END as Semestre
FROM (
	SELECT tender_id,
		cast(substring(date from 5 for 4) as integer) as year
	FROM tender_states
	WHERE state = '8') AA
group by Semestre;

-- DATO 3: PROVEEDORES PARTICIPANDO 

SELECT A.year,
	count(A.compId)
FROM
	(SELECT distinct company_id as compId,
		cast(substring(S.fecha from 5 for 4) as integer) as year
	FROM adjudication_items A
	LEFT JOIN tender_items B
	on A.tender_item_id = B.id
	INNER JOIN (
		SELECT 	tender_id as tenderId,
				date as fecha
		FROM tender_states
		WHERE state = '8'
	) S
	on B.tender_id= S.tenderId
	order by company_id) A
GROUP BY year;

-- DATO 4: ORGANISMOS LICITADORES 

SELECT ministerio,
	CASE WHEN year = '2013' THEN 'Y1'
	WHEN year = '2014' THEN 'Y2'
	ELSE 'Y3' END as Semestre
FROM temp4 XYZ
group by Semestre;





