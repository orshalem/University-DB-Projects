import mysql.connector

# This script lists all drivers who either won a race for 'Ferrari'
# or whose name code is 'FRA'. Results are distinct and sorted.

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()

    # SQL query to retrieve distinct drivers by condition
    cursor.execute("""
    SELECT DISTINCT Winner AS driver
FROM winners
WHERE Car = 'Ferrari'

UNION

SELECT DISTINCT Driver AS driver
FROM drivers
WHERE Nationality = 'FRA'

ORDER BY driver;
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))
