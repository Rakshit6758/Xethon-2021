from mysql.connector.cursor import MySQLCursor
from mysql_connector import database as mydb
import mysql
def transaction(info):
    try:
        mycursor = mydb.cursor()  
        # sql = f"select balance from banking_dataser where account_number={info[0]}"
        
        account1 = mycursor.execute(f"select balance from banking_dataset where account_number={info[0]}")
        account2 = mycursor.execute(f"select balance from banking_dataset where account_number={info[1]}")
        
        account1 = int(account1)-info[3]
        account2 = int(account2)+info[3]
        mycursor.execute(f"UPDATE banking_dataset SET balance = {account1} WHERE account_number = {info[0]}")
        mycursor.execute(f"UPDATE banking_dataset SET balance = {account2} WHERE account_number = {info[1]}")
        
        mydb.commit()
        mycursor.close()
        return "Amount transfer Successfully"
    
    except  mysql.connector.Error as error:
        return error
    
    
# info = [101,"Rithik","Choudhary","burnt776@gmail.com","male",1234567890,"savings","true",500000.00]
info = [1234567890,1234567890,10000]
print(transaction(info))
