select * from (select path, ip, status, count (*) as a from log
group by path, ip, status
order by a) as q1
where status like '20%'