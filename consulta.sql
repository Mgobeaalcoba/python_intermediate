select * from database_servicecenter
where date_inhub = '27-12-2021' and
date_dispatch = '28-12-2021'
group by hub_status
order by shipment_id;
