import mysql.connector
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory"
   
)
mycursor= mydb.cursor()
'''mycursor.execute("create database inventory")
print("Database  created successfully.")'''

mycursor.execute("create table invention (id int(2) primary key Auto_Increment, Name varchar (155), Model no varchar(155), Inventor varchar(10), Date of Issuevarchar(120))")
print("Table created successfully.")
'''sql ="insert into invention ( id, Name, Model no, Inventor, Date of Issue) values(%s,%s,%s,%s,%s)"
val=[
    ('',"Helicopter","o4","Simi","15/7/2006"),
    ('',"Aeroplane","hh9","Deeya","9/3/2004"),
    ('',"Ship","ik67","Riki","10/7/2004")
]
mycursor.execute(sql,val)
mydb.commit()
print("Data inserted successfully")'''