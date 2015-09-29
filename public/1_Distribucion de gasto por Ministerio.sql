/* PIE CHART POR MINISTERIO  */

SELECT 	WAP.label,
	sum(WAP.totalMonto) as totalMonto
FROM (
	SELECT 	XY.name ||'‐'|| XY.sub_name as label,
		Q.itemQuant * QQ.tipo_cambio as totalMonto,
		MM.region_unidad as region,
		cast(substring(S.fecha from 3 for 2) as integer) as month,
		cast(substring(S.fecha from 5 for 4) as integer) as year
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
	LEFT JOIN public_hierarchy XY
	on MM.code = XY.company_code) WAP
group by label
order by totalMonto DESC;



/* PIE CHART POR MINISTERIO POR AÑO Y REGION */

--  
SELECT 	WAP.label,
	sum(WAP.totalMonto) as totalMonto,
	CASE WHEN month <= '6' AND year = '2013' THEN 'S1'
	WHEN month > '6' AND year = '2013' THEN 'S2'
	WHEN month <= '6' AND year = '2014' THEN 'S3'
	WHEN month > '6' AND year = '2014' THEN 'S4'
	WHEN month <= '6' AND year = '2015' THEN 'S5'
	ELSE 'S6' END as Semestre,
	WAP.region as region
FROM (
	SELECT 	XY.name ||'‐'|| XY.sub_name as label,
		Q.itemQuant * QQ.tipo_cambio as totalMonto,
		MM.region_unidad as region,
		cast(substring(S.fecha from 3 for 2) as integer) as month,
		cast(substring(S.fecha from 5 for 4) as integer) as year
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
	LEFT JOIN public_hierarchy XY
	on MM.code = XY.company_code) WAP
group by label, Semestre, region
order by Semestre 

