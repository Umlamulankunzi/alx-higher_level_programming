-- Lists all records of the table second_table with a name value.
-- Order results by score in Desc order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
