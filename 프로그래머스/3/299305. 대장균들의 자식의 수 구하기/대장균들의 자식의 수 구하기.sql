-- 코드를 작성해주세요

select A.id, count(B.id) as CHILD_COUNT from ECOLI_DATA A
left join ECOLI_DATA B on A.id = B.parent_id
group by A.id