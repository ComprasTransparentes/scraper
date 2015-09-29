/* RANKING DE EMPRESAS QUE MAS DINERO HAN CONSEGUIDO */

SELECT 	AA.companyId as companyId,
	sum(AA.totalMonto) as monto
FROM (
		SELECT 	Q.tenderId as tenderId,
			Q.itemId as itemId,
			Q.companyId as companyId,
			Q.itemQuant * Q.itemMontoUnit * QQ.tipo_cambio as totalMonto,
			cast(substring(S.fecha from 1 for 2) as integer) as day,
			cast(substring(S.fecha from 3 for 2) as integer) as month,
			cast(substring(S.fecha from 5 for 4) as integer) as year
		FROM (
			SELECT A.id as itemId,
					CASE WHEN cast(B.cantidad as float) < cast(A.cantidad as float) THEN cast(B.cantidad  as float) ELSE cast(A.cantidad as float) END as itemQuant,
				cast(A.monto_unitario as float) as itemMontoUnit,
				A.company_id as companyId,
				B.tender_id as tenderId
			FROM adjudication_items A
			LEFT JOIN tender_items B
			on A.tender_item_id = B.id
			) Q
		LEFT JOIN tenders R
		on R.id = Q.tenderId
		INNER JOIN (
			SELECT 	tender_id as tenderId,
					date as fecha
			FROM tender_states
			WHERE state = '8'
		) S
		on Q.tenderId = S.tenderId
		LEFT JOIN currency QQ
		on QQ.moneda = R.moneda
	) AA
group by AA.companyId
order by sum(AA.totalMonto) DESC
LIMIT 15

/* RANKING DE EMPRESAS QUE MAS DINERO HAN CONSEGUIDO EN CADA SEMESTRE */

-- nota: cambiar la asignacion de semestres al pasar a produccion


DROP TABLE IF EXISTS temp1;

CREATE TEMP TABLE temp1 AS
SELECT 	AA.companyId as companyId,
	sum(AA.totalMonto) as monto,
	CASE WHEN day = '10' THEN 'S1'
		WHEN day = '11' THEN 'S2'
		ELSE 'S3' END as Semestre
FROM (
		SELECT 	Q.tenderId as tenderId,
			Q.itemId as itemId,
			Q.companyId as companyId,
			Q.itemQuant * Q.itemMontoUnit * QQ.tipo_cambio as totalMonto,
			cast(substring(S.fecha from 1 for 2) as integer) as day,
			cast(substring(S.fecha from 3 for 2) as integer) as month,
			cast(substring(S.fecha from 5 for 4) as integer) as year
		FROM (
			SELECT A.id as itemId,
					CASE WHEN cast(B.cantidad as float) < cast(A.cantidad as float) THEN cast(B.cantidad  as float) ELSE cast(A.cantidad as float) END as itemQuant,
				cast(A.monto_unitario as float) as itemMontoUnit,
				A.company_id as companyId,
				B.tender_id as tenderId
			FROM adjudication_items A
			LEFT JOIN tender_items B
			on A.tender_item_id = B.id
			) Q
		LEFT JOIN tenders R
		on R.id = Q.tenderId
		INNER JOIN (
			SELECT 	tender_id as tenderId,
					date as fecha
			FROM tender_states
			WHERE state = '8'
		) S
		on Q.tenderId = S.tenderId
		LEFT JOIN currency QQ
		on QQ.moneda = R.moneda
	)AA
group by AA.companyId, Semestre;

(select * from temp1 where semestre = 'S1' order by monto DESC limit 15)
union all
(select * from temp1 where semestre = 'S2' order by monto DESC limit 15)
union all
(select * from temp1 where semestre = 'S3' order by monto DESC limit 15)
