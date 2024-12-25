-- 코드를 작성해주세요

select B.year, B.max_val - A.SIZE_OF_COLONY as YEAR_DEV, A.id from ECOLI_DATA A

left join (select year(DIFFERENTIATION_DATE) as year, max(SIZE_OF_COLONY) as max_val
from ECOLI_DATA 
group by year(DIFFERENTIATION_DATE)) B on year(A.DIFFERENTIATION_DATE) = B.year
order by B.year, YEAR_DEV