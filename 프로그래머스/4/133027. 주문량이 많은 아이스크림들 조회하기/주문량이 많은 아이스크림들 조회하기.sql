-- 코드를 입력하세요


--상반기 주문 정보 FIRST_HALF : FLAVOR, SHIPMENT_ID, TOTAL_ORDER
--7월 주문 JULY :SHIPMENT_ID, FLAVOR, TOTAL_ORDER

-- SELECT Fh.FLAVOR, sum(FH.total_order)+ sum(Ju.total_order) as hap
-- from FIRST_HALF FH
-- left join JULY JU on FH.FLAVOR = JU.FLAVOR
-- group by Fh.flavor;



-- SELECT JU.FLAVOR, FH.total_order, Ju.total_order
-- from JULY JU
-- left join FIRST_HALF FH on FH.FLAVOR = JU.FLAVOR
-- ;

--, sum(fh.total_order) as half_total, sum(july_total)


select flavor 
from (
    select flavor, sum(total_order)
from (
    select flavor, total_order from FIRST_HALF FH
    union all 
    select flavor, total_order from JULY JU
    ) A
    group by flavor
    order by sum(total_order) desc
) B
where rownum <= 3;


