-- 코드를 입력하세요
SELECT ANIMAL_TYPE, COUNT(*) AS COUNT
FROM ANIMAL_INS
WHERE ANIMAL_TYPE='Cat' or ANIMAL_TYPE='Dog'
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE ASC