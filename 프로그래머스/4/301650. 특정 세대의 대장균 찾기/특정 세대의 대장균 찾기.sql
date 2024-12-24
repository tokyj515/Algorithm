-- 코드를 작성해주세요

SELECT 
    C.id 
FROM ECOLI_DATA A
LEFT JOIN ECOLI_DATA B ON A.id = B.parent_id and A.parent_id is null
LEFT JOIN ECOLI_DATA C ON B.id = C.parent_id
where C.id is not null
order by C.id

# SELECT 
#     A.id AS `1st`, 
#     B.id AS `2nd`, 
#     C.id AS `3rd`
# FROM ECOLI_DATA A
# LEFT JOIN ECOLI_DATA B ON A.id = B.parent_id and A.parent_id is null
# LEFT JOIN ECOLI_DATA C ON B.id = C.parent_id
# where C.id is not null
