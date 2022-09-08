-- list records with the same score in the
SELECT score,
       COUNT(*) AS number FROM second_table
       GROUP BY score
       ORDER BY score DESC;
