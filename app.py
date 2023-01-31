from datetime import datetime

# Connects python to mysql
pword = input("Enter password: ") # asks for the user's MariaDB password
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=pword,
    database="workspacedb")
mycursor = mydb.cursor()

def insertdutyData(): # function for adding a duty
    pass

def insertfield(): # function for adding a field
    pass

def selectAllfield(): # function for viewing all fieldories
    pass

def selectAlldutyData(): # function for viewing all dutys
    pass

def selectduty(): # function for viewing a duty
    pass

def editduty(dutyID): # function for editing and deleting a duty
    pass
     
def selectfield(): # function for viewing a field
    pass

def editfield(fieldID): # function for editing and deleting a field
    pass

while True: # Main Menu
   pass
    
