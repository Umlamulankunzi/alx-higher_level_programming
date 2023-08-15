-- Displays the max temperature of each state.
-- Ordered by state name in Asc order [default].
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
