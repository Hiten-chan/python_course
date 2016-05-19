import sqlite3 as sql

query = "select Users.name, Orders.id, sum(price) as s from Users " \
        "inner join Goods on Goods.id = good_id " \
        "inner join GoodsInOrders on Orders.id = order_id " \
        "inner join Orders on Users.id = user_id " \
        "where Users.id = ? and Orders.paid = 0 " \
        "group by Orders.id " \
        "order by Orders.id"
      
    
def unpaid(user_id):
    with sql.connect("data.sqlite") as data:
        cur = data.cursor()
        answer = cur.execute(query, [user_id]).fetchall()
    return answer      
