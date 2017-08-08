import numpy as np
import pandas as pd
import os
import seaborn as sns
from apyori import apriori
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#aisles_df = pd.read_csv("/home/sh.aggarwal/Desktop/market_basket/input/aisles.csv/aisles.csv")
#departments_df = pd.read_csv("/home/sh.aggarwal/Desktop/market_basket/input/departments.csv/departments.csv")
orders_df = pd.read_csv("/home/sh.aggarwal/Desktop/market_basket/input/orders.csv/orders.csv")
#order_products_prior_df = pd.read_csv("/home/sh.aggarwal/Desktop/market_basket/input/order_products_prior.csv/order_products_prior.csv")
#order_products_train_df = pd.read_csv("/home/sh.aggarwal/Desktop/market_basket/input/order_products_train.csv/order_products_train.csv")
#products_df = pd.read_csv("/home/sh.aggarwal/Desktop/market_basket/input/products.csv/products.csv")
#csv_file = "/home/sh.aggarwal/Desktop/market_basket/input/orders.csv/orders.csv"
#print(order_products_prior_df.head())
csv_db = create_engine('sqlite:///csv_db.db')
#prior_csv_file = "/home/sh.aggarwal/Desktop/market_basket/input/order_products_prior.csv/order_products_prior.csv"
"""aisles_csv = "/home/sh.aggarwal/Desktop/market_basket/input/aisles.csv/aisles.csv"
department_csv = "/home/sh.aggarwal/Desktop/market_basket/input/departments.csv/departments.csv"
product_csv = "/home/sh.aggarwal/Desktop/market_basket/input/products.csv/products.csv"
csv_db = create_engine('sqlite:///csv_db.db')
chunksize = 100000
j = 1
for df in pd.read_csv(product_csv,chunksize=chunksize,iterator=True) :
	df  = df.rename(columns = {c : c.replace(' ','') for c in df.columns})
	df.index += j
	df.to_sql('products',csv_db,if_exists = 'append')
	j = df.index[-1] + 1"""

"""df = pd.read_sql_query('select order_dow,count(*) as count from orders group by order_dow',csv_db)
#print(df.columns.values)
sns.barplot(df["order_dow"],df["count"],alpha=0.5,color='r')
sns.plt.show()"""
"""df = pd.read_sql_query("select order_hour_of_day,count(*) as count from orders group by order_hour_of_day",csv_db)
sns.barplot(df["order_hour_of_day"],df["count"],alpha=0.7,color='r')
sns.plt.show()"""
"""df = pd.read_sql_query("select order_dow,order_hour_of_day,count(*) as count from orders group by order_dow,order_hour_of_day",csv_db)
df = df.pivot(index = 'order_dow',columns = 'order_hour_of_day',values = 'count')
sns.heatmap(df)
sns.plt.show()"""
"""df = pd.read_sql_query("select days_since_prior_order,count(*) as count from orders group by days_since_prior_order",csv_db)
sns.barplot(df["days_since_prior_order"],df["count"],alpha=0.8,color='r')
sns.plt.show()"""
"""df1 = pd.read_sql_query("select reordered,count(*) as count from prior_orders group by reordered",csv_db)
#print(sum(df1["count"]))
#print(df1)
print(df1["count"]/sum(df1["count"])*100)"""
#df = pd.read_sql_query("select * from prior_orders",csv_db)
#print(df)
"""df = pd.read_sql_query("select product_name,count(*) from prior_orders a left join products b on a.product_id = b.product_id group by product_name order by count(*) desc",csv_db)
print(df)""" 
#df = pd.read_sql_query("create table total as (select * from prior_orders a left join products b on a.product_id = b.product_id inner join departments c on b.department_id = c.department_id inner join aisles d on b.aisle_id = d.aisle_id)",csv_db)
"""df = pd.read_sql_query("select department,count(*) as count from total group by department",csv_db)
sns.barplot(df["department"],df["count"])
sns.plt.show()"""
"""df["count"] = (df["count"]/sum(df["count"]))*100
plt.pie(np.array(df["count"]),labels = np.array(df["department"]))
plt.show()"""
"""df = pd.read_sql_query("select count(product_id) from prior_orders group by order_id",csv_db)
print(df)"""
"""df = pd.read_sql_query("select product_id from products where product_name in ('Banana','Organic Strawberries','Bag of Organic Bananas','Organic Baby Spinach','Organic Hass Avocado')",csv_db)
print(df)"""
#df = pd.read_sql_query("select order_id from orders where eval_set = 'test'",csv_db)
orders_df = orders_df[orders_df["eval_set"] == 'test']
with open("/home/sh.aggarwal/Desktop/market_basket/sub1.csv",'w') as f :
	f.write(str(orders_df["order_id"]))
