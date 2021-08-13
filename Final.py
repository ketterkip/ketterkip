import psycopg2

"""connection to the DataBase"""
con = psycopg2.connect(
    host="localhost",
    database="dvdrental1",
    user="postgres",
    password="123456",
    port="5432")
# cursor
cur = con.cursor()

"""execute query to output customer_name, address, email"""

cur.execute("select first_name, last_name, address_id, email, customer_id from customer")

results = cur.fetchall()
def payment(customer_id):
    pay_list = []
    """execute query to output customer_id_1, staff_id, rental_id"""
    cur.execute(f"select customer_id_1, staff_id, rental_id from payment where customer_id_1 = {customer_id}")
    pay = cur.fetchall()
    for j in pay:
        pay_dict = {}
        pay_dict['customer_id'] = j[0]
        pay_dict['staff_id'] = j[1]
        pay_dict['rental_id'] = j[2]
        pay_list.append(pay_dict)
    return pay_list

customer_list = []
for customer in results[:1]:
    # print(customer)
    combined_dict = {}
    combined_dict['customer name'] = customer[0] + ' ' + customer[1]
    combined_dict['address'] = customer[2]
    combined_dict['email'] = customer[3]
    """execute query to output inventory_id"""
    cur.execute(f"select inventory_id from rental where rental_id = {customer[4]}")

    try:
        inventory_id = cur.fetchall()[0][0]
    except IndexError:
        print(customer)

    cur.execute(f"select film_id from inventory where inventory_id = {inventory_id}")
    film_id = cur.fetchall()
    # print(film_id)

    cur.execute(f"select title, description, rental_duration from film where film_id = {film_id[0][0]}")
    sects = cur.fetchall()
    film_sect = {}
    film_sect['title'] = sects[0][0]
    film_sect['description'] = sects[0][1]
    film_sect['rental_duration'] = sects[0][2]

    for store_sec in customer:
        cur.execute(f"select address_id from address where address_id = {customer[2]}")
        addr = cur.fetchall()

        # print(addr)
        cur.execute(f"select * from store where address_id = {addr[0][0]}")
        store_id_1 = cur.fetchall()

        # cur.execute(f"select store_id, manager_staff_id from store where store_id = {store_id_1[0]}")
        # store_a = cur.fetchall()
        # print(store_a)


    combined_dict['film_section'] = film_sect
    combined_dict['payment'] = payment(customer_id=customer[4])

    # print(combined_dict)

    customer_list.append(combined_dict)

print(customer_list)


