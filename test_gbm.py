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
#print(orders_df.head())
#prior_csv_file = "/home/sh.aggarwal/Desktop/market_basket/input/order_products_prior.csv/order_products_prior.csv"
#df = pd.read_sql_query("create table temp as select product_id,aisle_id,department_id,count(*) as orders,sum(reordered) as reorders,sum(reordered)/count(*) as reorder_ratio from total group by product_id",csv_db)
#df["reorder_ratio"] = df["reorders"]/df["orders"]
#print(df.head())
#df = pd.read_sql_query("select * from orders where order_id = 1",csv_db)
#df_final = pd.read_sql_query("create table analysis as select * from prior_orders a inner join orders b on a.order_id = b.order_id",csv_db)
#print(df_final.head())
#pd.read_sql_query("create index idx3 on analysis(user_id)",csv_db)
#pd.read_sql_query("create index idx4 on analysis(product_id,user_id)",csv_db)
#df = pd.read_sql_query("select * from analysis where order_id = 75",csv_db)
#print(df.head())


#df = pd.read_sql_query("select sum(days_since_prior_order)/count(days_since_prior_order) as average_days_between_orders,count(distinct order_id) as nb_orders from orders group by user_id",csv_db)
#print(df.head())



df = pd.read_sql_query("select count(order_id) from analysis group by user_id",csv_db)
print(df)




#df = pd.read_sql_query("select type, name, tbl_name, sql FROM sqlite_master WHERE type='index'",csv_db)
#print(df)


#df = pd.read_sql_query("select count(b.product_id) as total_items,count(distinct b.product_id) as total_distinct_items,group_concat(b.product_id) as all_products from orders a left join prior_orders b on a.order_id = b.order_id  group by a.user_id",csv_db)
#print(df.head())
