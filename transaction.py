from mysql.connector.cursor import MySQLCursor
from mysql_connector import database as mydb
import mysql
def transaction(info):
    try:
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="bank"
            )
        # return mydb
   
        
        mycursor = mydb.cursor()  
        # sql = f"select balance from banking_dataser where account_number={info[0]}"
        
        mycursor.execute(f"select balance from banking_dataset where account_number={info[0]}")
        account1 = mycursor.fetchall()
        mycursor.execute(f"select balance from banking_dataset where account_number={info[1]}")
        account2 = mycursor.fetchall()
        print(account2)
        account1 = int(int(account1)-info[3])
        account2 = int(int(account2)+info[3])
        mycursor.execute(f"UPDATE banking_dataset SET balance = {account1} WHERE account_number = {str(info[0])}")
        mycursor.execute(f"UPDATE banking_dataset SET balance = {account2} WHERE account_number = {str(info[1])}")
        
        mydb.commit()
        mycursor.close()
        return "Amount transfer Successfully"
    
    except  mysql.connector.Error as error:
        return error
    
    
# info = [101,"Rithik","Choudhary","burnt776@gmail.com","male",1234567890,"savings","true",500000.00]
info = [1234567890,1234567890,10000]
print(transaction(info))
