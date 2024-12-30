-- 코드를 작성해주세요
select year(YM) as year, round(avg(PM_VAL1), 2) as `PM10`, round(avg(PM_VAL2), 2) as `PM2.5`
from AIR_POLLUTION 
where LOCATION2 like '수원' 
group by year(YM)
order by year(YM)


