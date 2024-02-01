import mysql.connector as myconn
mydb = myconn.connect(
    host="bzww6voywepttascpl44-mysql.services.clever-cloud.com",
    user="uf9srr9rwtttokwi",
    password="SLk5emfZrpnqSMwspuyU",
    database="bzww6voywepttascpl44")


db_cursor = mydb.cursor()
db_cursor.execute("SELECT LR FROM subdata")
for i in db_cursor:
    print(i)
