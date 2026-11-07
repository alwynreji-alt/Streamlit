from itertools import product

import mysql.connector
# # # or from mysql import connector (This can also to be used for calling.)
# con=mysql.connector.connect(user="root",password="root",host="localhost")
# # # establish connection between python code and mysql server
# # # it returns a connection object
# c=con.cursor() # used to execute sql queries/commands
# c.execute("create database school_db")
# print("Database File executed")
#
# con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")
# c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,
# name varchar(20),
# age int,
# place varchar(20),
# phone varchar(20),
# total_mark int)''')
# print("table created successfully")
# c.execute('''
# insert into student(roll_no,name,age,place,phone,total_mark)
# values(101,"arun",11,'ekm','734398929',145),
# (102,"amal",12,'ekm','7343458929',140),
# (103,"anu",12,'tcr','8922322345',147),
# (104,"hari",11,'ekm','734398929',144),
# (105,"manu",11,'ekm','8328433423',141)
# ''');


# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"

# qwen=(106,'alwyn',22,'koty','7492732930',190)
# c.execute(query,qwen)
#
# con.commit() # to save data permanently inside_db
# print("Data Inserted")
# #
# query ="select * from student"
# c.execute(query)
# #
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("no record found")







# id=int(input("enter the id:" ))
# query="select * from student where roll_no=%s"
# data=(id,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print("no record found")





# update mark of a student with roll no= roll no by the user

# roll_no=int(input("enter the roll:" ))
# mark=int(input("enter the mark:" ))
# query="UPDATE student SET total_mark = %s WHERE roll_no = %s"
# data=(mark,roll_no)
# c.execute(query,data)
# con.commit()





# roll_no=input("enter the roll:" )
#
# query="delete from student WHERE roll_no = %s"
# data=(roll_no,)
# c.execute(query,data)
# con.commit()






#
# create a new record using values entered by user



# roll_no=int(input(" enter the roll number:"))
# name=input("enter the name:")
# age=int(input("enter the age"))
# place=input("enter the place:")
# phone=int(input("enter the phone number:"))
# total_mark=int(input("enter the total mark:"))
# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
# data=(roll_no, name, age, place, phone, total_mark)
# c.execute(query,data)
# con.commit()
#
# query ="select * from student"
# c.execute(query)
# #
# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("no record found")






# con=mysql.connector.connect(user="root",password="root",host="localhost")
# c=con.cursor()
# c.execute("create database shop")
# print("Database File executed")


import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="shop"
)
#
c = con.cursor()
#
# c.execute('''
# CREATE TABLE product (
#     product_id INT NOT NULL PRIMARY KEY,
#     name VARCHAR(20),
#     brand VARCHAR(20),
#     category VARCHAR(20),
#     price INT,
#     stock INT
# )
# ''')

# c.execute('''
# INSERT INTO product
# (product_id, name, brand, category, price, stock)
# VALUES
# (101, 'Laptop', 'Dell', 'Electronics', 55000, 10),
# (102, 'Smartphone', 'Samsung', 'Electronics', 25000, 15)
# ''')

# con.commit()

while True:
    print("\n---------shop--------")
    print("1.insert product detail")
    print("2.Read all Product details")
    print("3.SearchaProductbyproduct_id")
    print("4.Update the stock of a Product")
    print("5.Delete a Product record")
    print("6.Exit")


    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_id = int(input("Enter product id: "))
        name = input("Enter product name: ")
        brand = input("Enter brand: ")
        category = input("Enter category: ")
        price = int(input("Enter price: "))
        stock = int(input("Enter stock: "))

        query = "insert into student(product_id, name, brand, category, price, stock)values(%s,%s,%s,%s,%s,%s)"

        data =(product_id, name, brand, category, price, stock)
        c.execute(query,data)
        con.commit()



