-- Displays the average temperature (in Fahrenheit)
-- By city ordered by temperature in Desc Order.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
