-- The Lists of number  recording the same score in the table s'econd_table'.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
