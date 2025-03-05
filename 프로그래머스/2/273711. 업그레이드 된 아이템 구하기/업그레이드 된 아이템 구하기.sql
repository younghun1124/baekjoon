-- 코드를 작성해주세요
SELECT I.ITEM_ID AS ITEM_ID, I.ITEM_NAME AS ITEM_NAME, I.RARITY AS RARITY
FROM ITEM_TREE T
JOIN (SELECT ITEM_ID
FROM ITEM_INFO
WHERE RARITY='RARE') RI-- 레어 아이템 아이디
ON RI.ITEM_ID=T.PARENT_ITEM_ID
JOIN ITEM_INFO I
ON T.ITEM_ID=I.ITEM_ID
ORDER BY I.ITEM_ID DESC