import json

import psycopg2
#connection to the DataBase
con = psycopg2.connect(
        host = "localhost",
        database = "dvdrental",
        user = "postgres",
        password = "123456",
        port = "5432")
#cursor
cur = con.cursor()
#execute query to output customer_name, address, email
cur.execute("select first_name, last_name, address_id, email from customer")

rows = cur.fetchall()
print(rows)
for values in rows:
    cust = {
        "first_name": values[0],
        "last_name": values[1],
        "address": values[2],
        "email": values[3]
    }

    #print(cust)

#execute query to output from payment table
cur.execute("select customer_id, staff_id, rental_id from payment")

rows = cur.fetchall()

"""loop through the tuple"""
for values in rows:
         cust = {
             "customer_id":values[0],
             "staff_id":values[1],
             "rental_id":values[2],
         }
         #print(pay)


#execute query to output queried data from film_section
cur.execute("select title, description, rental_duration from film")

rows = cur.fetchall()

for values in rows:
         ent = {
             "title":values[0],
             "description":values[1],
             "rental_duration":values[2],
         }

         #print(ent)

"""create list"""
#store_list = [pay, ent]
#print(store_list)

# a query to output store data
cur.execute("select store_id, manager_staff_id from store")

rows = cur.fetchall()
"""create list"""
#store_list=[]
for values in rows:
    store_sect = {
            "store_id":null[0],
            "manager_staff_id":null[1]
         }
    #print(store_sect)
    #store_list = store_sect.append(cust)
    #print(store_list)

    #print(store_sect)

#print(store_list)

#close the cursor
cur.close()

#close the connection
con.close()

#handle null in pthon

store_sect = '{"store_is":null, "management_staff_id":null}'
#print(store_sect)

"""merge the lists"""
#storage = {**ent, **pay, **store_sect}
#print(storage)

#parse the data

dict = json.loads(store_sect)
#print(dict)

"""Read to JSON File"""


"""Combined of all outpu"""
j = json.dumps(dict)
with open("MyStore.json.json", 'w') as f:
    f.write(j)
    f.close()