SELECT
  tu.shp_lg_tr_related_entity_id ShipmentID,
  otu.SHP_LG_SCAN_DATETIME Hora_Picked,
  rs.shp_lg_stop_id ID_de_parada,
  tu.shp_logistic_type Tipo_Colecta,
  r.shp_lg_route_id ID_Ruta,
  r.shp_lg_code Nombre_Ruta,
  r.shp_lg_init_date Fecha_Ruta,
  C.shp_company_name Transportadora,
  r.shp_lg_vehicle_plate_id Patente,
  r.shp_lg_facility_id Deposito,
  C.shp_co_site_id Site,
  tu.shp_lg_tr_related_entity_type tipo_paquete

FROM
  WHOWNER.LK_SHP_LG_ROUTES AS r
INNER JOIN  WHOWNER.LK_SHP_LG_ROUTE_STOP AS rs ON (r.shp_lg_route_id  = rs.shp_lg_route_id)
INNER JOIN  WHOWNER.BT_SHP_LG_ORDER AS o  ON (o.shp_lg_route_stop_id  = rs.shp_lg_stop_id)
INNER JOIN  WHOWNER.LK_SHP_LG_ORDER_TU AS otu ON (otu.shp_lg_order_id  = o.shp_lg_order_id)
INNER JOIN  WHOWNER.lk_shp_companies AS C ON (c.shp_company_id = r.shp_company_id)
INNER JOIN  WHOWNER.lk_shp_lg_transport_unit tu ON (otu.shp_lg_transport_unit_id = tu.shp_lg_transport_unit_id)
WHERE
  otu.shp_lg_transport_unit_status in ('picked_up')
and r.shp_lg_route_status like 'close'
and r.shp_lg_type like 'first_mile'
and c.shp_co_site_id = 'MLA'
-- and r.shp_lg_facility_id = 'ARBA01'
-- and c.shp_company_name = 'Loginter'
-- and  r.shp_lg_vehicle_plate_id Patente in ('')
--and tu.shp_lg_tr_related_entity_id in ('')
AND CAST(r.shp_lg_init_date as date) = '2021-09-13'
