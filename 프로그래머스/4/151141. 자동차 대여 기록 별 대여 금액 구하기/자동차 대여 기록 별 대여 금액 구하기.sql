WITH TR AS (
    SELECT 
        C.CAR_TYPE, 
        H.START_DATE, 
        H.END_DATE, 
        H.HISTORY_ID, 
        C.CAR_ID, 
        C.DAILY_FEE, 
        CASE
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 90 THEN '90일 이상'
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 30 THEN '30일 이상'
            WHEN DATEDIFF(H.END_DATE, H.START_DATE) + 1 >= 7 THEN '7일 이상'
        END AS DURATION_TYPE,
        DATEDIFF(H.END_DATE, H.START_DATE) + 1 AS DURATION
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    JOIN CAR_RENTAL_COMPANY_CAR C
    ON C.CAR_ID = H.CAR_ID
    WHERE C.CAR_TYPE = '트럭'
)

SELECT 
    TR.HISTORY_ID,
    TRUNCATE(
        TR.DAILY_FEE * TR.DURATION * 
        (1 - (IFNULL(CAST(REPLACE(P.DISCOUNT_RATE, '%', '') AS DECIMAL(5,2)), 0) / 100)), 
        0
    ) AS FEE
FROM TR
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
ON TR.DURATION_TYPE = P.DURATION_TYPE AND TR.CAR_TYPE = P.CAR_TYPE
ORDER BY FEE DESC, TR.HISTORY_ID DESC;
