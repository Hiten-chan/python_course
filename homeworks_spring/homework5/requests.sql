1) Всю информацию о всех пользователях (все колонки в любом
порядке)

select * from users;


2) Количество всех пользователей (число)

select users.name, count(*) from users;


3) Количество пользователей 40 лет или старше (число). Чтобы
сравнить столбец таблицы с конкретной датой можно использо-
вать функцию date – where birth_date <= date(”2000-12-20”) с да-
той в формате ”YYYY-MM-DD”.

select users.name, birth_date, count(*) from users 
where birth_date <= date('1976-05-20');


4) Страна + количество пользователей из данной страны (стра-
на|количество)

select users.country, count(*) from users 
group by country;


5) Придумайте, как проверить, есть ли люди с одинаковым именем
(в любом удобном формате)

select users.name, count(*) as c from users 
group by name 
order by c desc limit 1;


6) Количество заказов в 2016 году (число)

select orders.created datetime, count(*) from orders 
where created >= '2016-01-01 00:00:00';


7) День, когда совершили наибольшее число заказов (день|число
заказов)

select date(created) as f, count(*) as a from orders 
group by f 
order by a desc limit 1;


8) Процент неоплаченных заказов (число)

select 100 * sum (case paid when 0 then 1 else 0 end) / count(paid) from orders;


9) Всю информацию о хлебе среди товаров. Используйте конструк-
цию where name like ”%bread%”. Ссылка. (все колонки в любом
порядке)

select * from goods where name like '%bread%';


10) Самые 10 популярных товаров (встречаемость в GoodsInOrders)
(id|name|количество)

select goods.id, goods.name, count(*) as a from goodsinorders 
inner join goods on good_id = id 
group by good_id 
order by a desc 
limit 10;


11) Чистая выручка в 2016 году. Нужно учитывать только оплачен-
ные заказы (число)

select sum(price) from goods 
inner join orders on orders.id = order_id 
inner join goodsinorders on goods.id = good_id 
where paid = 1;


12) Самые 10 популярных товаров среди женщин (id|название)

select Goods.id, Goods.name from Goods 
inner join Users on Users.id = user_id 
inner join Orders on order_id = Orders.id 
inner join GoodsInOrders on Goods.id = good_id 
where gender = "F" 
group by Goods.name 
order by count(*) desc 
limit 10;


13) Пользователь, который купил больше всего килограмм (id|имя)

select Users.id, Users.name from Users 
inner join Goods on Goods.id = good_id 
inner join GoodsInOrders on Orders.id = order_id
inner join Orders on Users.id = user_id 
where units = "KG" 
group by user_id 
order by sum(Goods.quantity) desc 
limit 1;

