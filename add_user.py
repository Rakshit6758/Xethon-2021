from mysql.connector.cursor import MySQLCursor
from mysql_connector import database as mydb
import mysql

print(mydb)
def user_info(info):
    try:
        mycursor = mydb.cursor()  
           
        val = (info)
        sql = "INSERT INTO BANKING_DATASET(id,first_name,last_name,email,gender,account_number,account_type,on_hold,balance) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s)"
        
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        return "created account successfully"
    
    except  mysql.connector.Error as error:
        return error
    
    
info = [101,"Rithik","Choudhary","burnt776@gmail.com","male",1234567890,"savings","true",500000.00]

print(user_info(info))
