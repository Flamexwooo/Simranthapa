#create databse mysql# 
import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)
mycursor= mydb.cursor()
'''mycursor.execute("create database student")
print("Database created successfully.")
mycursor.execute("create table students (id int(2) primary key Auto_Increment, name varchar (155), address varchar(155), phone varchar(10), contact_person varchar(120))")
print("Table created successfully.")'''
mycursor= mydb.cursor()
sql ="insert into students ( id, name, address, phone, contact_person) values(%s,%s,%s,%s,%s)"
val=[
    ('',"Suraj Tamang","Mirik","8653833318","Mr.Binod Tamang"),
    ('',"Sanskriti Dewan Sunar","Siliguri","1234567890","Mr.Basant Sunar")
]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")