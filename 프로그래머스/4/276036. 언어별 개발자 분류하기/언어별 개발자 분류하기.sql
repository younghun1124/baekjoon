SELECT *
FROM(
SELECT 
CASE
WHEN FIND_IN_SET('PYTHON', GROUP_CONCAT(NAME))>0
 AND FIND_IN_SET('FRONT END', GROUP_CONCAT(CATEGORY))>0  THEN 'A'
WHEN FIND_IN_SET('C#',GROUP_CONCAT(NAME))>0 THEN 'B'
WHEN FIND_IN_SET('FRONT END', GROUP_CONCAT(CATEGORY))>0 THEN 'C'
END AS GRADE,
D.ID,
D.EMAIL
FROM DEVELOPERS D
LEFT JOIN SKILLCODES S
ON S.CODE&D.SKILL_CODE>0
GROUP BY D.ID,D.EMAIL
ORDER BY GRADE ASC, D.ID ASC
    )T
WHERE T.GRADE IS NOT NULL