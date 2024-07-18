-- 코드를 입력하세요
-- 입양을 못 간 동물 -> in은 있고 out은 없는 동물
-- inner join하면 in있고 out있음 -> 입양 감
-- 가장 오래 보호소에 있던 동물 3마리 
-- SELECT ANIMAL_INS.NAME, ANIMAL_INS.DATETIME from ANIMAL_INS
-- where ANIMAL_INS.ANIMAL_ID not in (select I.ANIMAL_ID 
--                         from ANIMAL_INS I
--                         join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID)
--         and rownum <= 3
-- order by ANIMAL_INS.datetime

select I.NAME, I.DATETIME from ANIMAL_INS I
left join ANIMAL_OUTS O on I.ANIMAL_ID = O.ANIMAL_ID
where O.ANIMAL_ID is null
order by I.datetime
FETCH FIRST 3 ROWS ONLY;