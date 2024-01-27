import subprocess
import mysql.connector as myconn

# Specify the path to your program
program_path = r"E:\python files\sql\ex1.py"

# Run the program and capture its output
output_data = subprocess.getoutput(f'python "{program_path}"')
conv=int(output_data)

mydb = myconn.connect(
    host="bzww6voywepttascpl44-mysql.services.clever-cloud.com",
    user="uf9srr9rwtttokwi",
    password="SLk5emfZrpnqSMwspuyU",
    database="bzww6voywepttascpl44")

db_cursor = mydb.cursor()
db_cursor.execute("insert into webdata(value) values(%s)",(conv,))
mydb.commit()
print(db_cursor.rowcount,"record inserted")




