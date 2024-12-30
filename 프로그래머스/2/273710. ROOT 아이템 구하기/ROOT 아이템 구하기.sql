-- 코드를 작성해주세요
select A.ITEM_ID, B.ITEM_NAME from ITEM_TREE A
left join ITEM_INFO B on A.ITEM_ID = B.ITEM_ID
where PARENT_ITEM_ID is null
order by A.ITEM_ID