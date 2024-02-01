import subprocess
import mysql.connector as myconn

# Specify the path to your program
program_path = r"E:\python files\sql\ex1.py" # <- paste the learning rate calculation code's path in the double quotetion section 

# Run the program and capture its output
output_data = subprocess.getoutput(f'python "{program_path}"')
conv=double(output_data)

mydb = myconn.connect(
    host="bzww6voywepttascpl44-mysql.services.clever-cloud.com",
    user="uf9srr9rwtttokwi",
    password="SLk5emfZrpnqSMwspuyU",
    database="bzww6voywepttascpl44")

db_cursor = mydb.cursor()
# Update the LR column in the subdata table where Subjects is 'Queue'
update_query = f"UPDATE subdata SET LR = {conv} WHERE Subjects = 'Queue'"    #update the Queue , linled list those row names and re-insert
db_cursor.execute(update_query)
mydb.commit()
print(db_cursor.rowcount,"record inserted")
