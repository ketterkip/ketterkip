import json

import pandas as pd
import psycopg2
"""connection to the DataBase"""
con = psycopg2.connect(
        host = "localhost",
        database = "dvdrental",
        user = "postgres",
        password = "123456",
        port = "5432")
#cursor
cur = con.cursor()

"""execute query to output from payment table"""
cur.execute("select customer_id_1, staff_id, rental_id from payment")

rows = cur.fetchall()
# print(rows)

"""loop through the tuple"""
payments = []
for value in rows:
         pay = {
             "customer_id_1": value[0],
             "staff_id": value[1],
             "rental_id": value[2]
         }
         # print(pay)
         payments.append(pay)
# print(payments)

"""execute query to output queried data from film_section"""
cur.execute("select title, description, rental_duration from film")

rows = cur.fetchall()
film_section = []
for values in rows:
         ent = {
             "title": values[0],
             "description": values[1],
             "rental_duration": values[2]
         }
         # print(ent)
         film_section.append(ent)
# print(film_section)

# a query to output store data
cur.execute("select store_id, manager_staff_id from store")

rows = cur.fetchall()
"""create list"""
store_list={}

for values in rows:
    store_sect = {
            "store_id": [0],
            "manager_staff_id": [1]
         }
    store_list.update(store_sect)
# print(store_list)
"""execute query to output customer_name, address, email"""

cur.execute("select first_name, last_name, address_id, email from customer")

results = cur.fetchall()
#print(rows)
customers=[]
# combined_dict={}
for result in results:
    cust = {
        "first_name": result[0],
        "last_name": result[1],
        "address": result[2],
        "email": result[3]
    }
    # print(cust)
    # customers.update(cust)
    customers.append(cust)
# print(type(customers))
#
def customer_details(first_name):
    for customer in customers:
        if customer['first_name'] == "first_name":
            customers['last_name'] == "last_name"
            customers['address_id'] == "address_id"
            customers['email'] == "email"
        # where "first_name" = "first_name"
    # return customer

            sql = (
            f" {customers[first_name]}" \
            f" {customers[last_name]}" \
            f" {customers[address_id]}" \
            f" {customers[email]}"
            # from customers
        where first_name = 'customers'

            )
print(sql)
# def customer_details(first_name):
#     for customer in customers:
#         if customer['first_name'] == first_name:
#             return customer
# print(customer_details('Jared'))


# """"combining lists"""
# combined = []
# for pay in payments:
#     combined.append(payments)
# for custom in customers:
#     combined.append(customers)
# for film in film_section:
#     combined.append(film_section)
#
# print(combined)













































































































































































































































































































































































































































































































































































































































































































































































# #close the cursor
# cur.close()
#
# """close the connection"""
# con.close()
#
# """handle null in pthon"""
#
# store_sect = '{"store_is":null, "management_staff_id":null}'
# #print(store_sect)
#
# """merge the dictionaries"""
#
# storage = {**ent, **pay, **cust}
# #print(storage)

"""parse the data"""

# dict = json.loads(store_sect)
# #print(dict)
#
# """Read to JSON File"""
#
#
# """Combined of all output"""
# j = json.dumps(dict)
# with open("MyStore.json.json", 'w') as f:
#     f.write(j)
#     f.close()
