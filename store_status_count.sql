-- Create view for summing the status count per day
CREATE VIEW v_status_count AS
Select q1.date, q1.count, q2.count from

(SELECT
   count (*),
   TO_CHAR(time,'YYYY-MM-DD') as "date"

FROM log

GROUP BY TO_CHAR(time,'YYYY-MM-DD')

ORDER BY TO_CHAR(time,'YYYY-MM-DD') desc) as q1

,

(SELECT
   count (*),
   TO_CHAR(time,'YYYY-MM-DD') as "date"
FROM log
WHERE log.status not like '200 OK'
GROUP BY TO_CHAR(time,'YYYY-MM-DD')
ORDER BY TO_CHAR(time,'YYYY-MM-DD') desc ) as q2

WHERE q1.date = q2.date;

-- Create view joining the authors and articles table
CREATE VIEW v_list AS
SELECT authors.name, authors.id, articles.title,
log.method, log.status, log.time FROM authors, articles, log
WHERE log.path like concat('%',articles.slug,'%')
AND articles.author = authors.ID;

-- Just to make sure the view is accessible, set the owner of the view.
ALTER VIEW v_status_count OWNER TO vagrant;
ALTER VIEW v_list OWNER TO vagrant;
