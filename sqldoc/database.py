import mysql.connector as myconn
mydb = myconn.connect(
    host="bzww6voywepttascpl44-mysql.services.clever-cloud.com",
    user="uf9srr9rwtttokwi",
    password="SLk5emfZrpnqSMwspuyU")


db_cursor = mydb.cursor()
db_cursor.execute("show Databases") #to show the database
print(db_cursor.execute)