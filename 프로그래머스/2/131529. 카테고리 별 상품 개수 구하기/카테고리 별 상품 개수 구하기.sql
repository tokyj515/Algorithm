-- 코드를 입력하세요
SELECT substring(PRODUCT_CODE, 1, 2) as CATEGORY, count(PRODUCT_ID) as PRODUCTS
from PRODUCT
group by substring(PRODUCT_CODE, 1, 2)
order by substring(PRODUCT_CODE, 1, 2)