-- 코드를 작성해주세요
SELECT DISTINCT D.ID AS ID, D.EMAIL AS EMAIL, D.FIRST_NAME AS FIRST_NAME, D.LAST_NAME AS LAST_NAME

FROM SKILLCODES S
JOIN DEVELOPERS D
ON (D.SKILL_CODE&S.CODE)=S.CODE
WHERE S.CATEGORY="Front End"

ORDER BY D.ID ASC
