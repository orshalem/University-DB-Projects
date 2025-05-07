import mysql.connector

# This script retrieves the distinct list of drivers from Brazil.
# It queries the 'drivers' table where the Nationality is 'BRA'.

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT distinct Driver
        FROM drivers
        WHERE Nationality = 'BRA'
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
