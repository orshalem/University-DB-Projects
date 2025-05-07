import mysql.connector

if __name__ == '__main__':
    # Connect to MySQL server 
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3307
    )

    cursor = mydb.cursor()
    
    # Create the 'burgers' database 
    cursor.execute("CREATE DATABASE IF NOT EXISTS burgers;")
    
    cursor.close()
    mydb.close()
