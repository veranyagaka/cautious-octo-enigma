# Write your MySQL query statement below
select product_id, product_name, description
from products
where REGEXP_LIKE (
    description,
    '(?<![A-Za-z0-9])SN\\d{4}-\\d{4}(?![A-Za-z0-9])',
    'c'
)
order by product_id asc;
# negative lookahead and lookbehind, escaping char
