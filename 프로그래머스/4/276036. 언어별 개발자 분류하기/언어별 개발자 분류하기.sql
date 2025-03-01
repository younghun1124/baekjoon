WITH PY AS (
SELECT CODE
FROM SKILLCODES
WHERE NAME='Python'
),
FE AS(
SELECT SUM(CODE) AS CODE
FROM SKILLCODES
WHERE CATEGORY='Front End'
),
CS AS (
SELECT CODE
FROM SKILLCODES
WHERE NAME='C#'
)

SELECT *
FROM (SELECT 
    CASE
        WHEN (D.SKILL_CODE & PY.CODE)>0 AND (D.SKILL_CODE & FE.CODE) >0 THEN 'A'
        WHEN (D.SKILL_CODE & CS.CODE)>0 THEN 'B'
        WHEN (D.SKILL_CODE & FE.CODE)>0 THEN 'C'
        ELSE NULL
    END AS GRADE,
    D.ID AS ID,D.EMAIL AS EMAIL
FROM DEVELOPERS D
    CROSS JOIN PY
    CROSS JOIN FE
    CROSS JOIN CS
     ) T
WHERE GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC


