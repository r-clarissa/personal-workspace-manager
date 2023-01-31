# Connects python to mysql
user_pass = input('Enter password: ')
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=user_pass) # Change passwd to your personal MariaDB passwd

# Displays the connection log
if(mydb):
    print("\nSuccessfully connected.")
else:
    print("\nFailed to connect.")

# Setup the workspacedb
mycursor = mydb.cursor()
try:
    print("Database 'workspacedb' successfully created.")
except:
    print("Database creation failed or database already exists!")

# Creates field table
try:
    print("table 'field' successfully created.")
except:
    print("table 'field' creation failed.")

# Creates duty table
try:
    print("table 'duty' successfully created.")
except:
    print("table 'duty' creation failed.")

