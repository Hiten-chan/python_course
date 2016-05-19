1) select * from users;

2) select users.name, count(*) from users;

3) select users.name, birth_date, count(*) from users 
where birth_date <= date('1976-05-20');

4) select users.country, count(*) from users 
group by country;

5) select users.name, count(*) as c from users 
group by name 
order by c desc limit 1;

6) select orders.created datetime, count(*) from orders 
where created >= '2016-01-01 00:00:00';

7) select date(created) as f, count(*) as a from orders 
group by f 
order by a desc limit 1;

8) select 100 * sum (case paid when 0 then 1 else 0 end) / count(paid) from orders;

9) select * from goods where name like '%bread%';

10) select goods.id, goods.name, count(*) as a from goodsinorders 
inner join goods on good_id = id 
group by good_id 
order by a desc 
limit 10;

11) select sum(price) from goods 
inner join orders on orders.id = order_id 
inner join goodsinorders on goods.id = good_id 
where paid = 1;

12) select Goods.id, Goods.name from Goods 
inner join Users on Users.id = user_id 
inner join Orders on order_id = Orders.id 
inner join GoodsInOrders on Goods.id = good_id 
where gender = "F" 
group by Goods.name 
order by count(*) desc 
limit 10;

13) select Users.id, Users.name from Users 
inner join Goods on Goods.id = good_id 
inner join GoodsInOrders on Orders.id = order_id
inner join Orders on Users.id = user_id 
where units = "KG" 
group by user_id 
order by sum(Goods.quantity) desc 
limit 1;

