# Write your MySQL query statement below
select DISTINCT p.product_id, p.product_name

from Product p
inner join Sales s
    on p.product_id = s.product_id

where sale_date between '2019-01-01' and '2019-03-31'

    and not exists (
        select 1
        from Sales s2
        where s2.product_id = s.product_id
        and s2.sale_date not between '2019-01-01' and '2019-03-31'

    );