import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port='3307',
    )
    cursor = mydb.cursor()

    # Create the 'city' table to store city information
    cursor.execute("""
        CREATE TABLE city (
            city_id INT PRIMARY KEY,
            city_name VARCHAR(255) NOT NULL
            );
    """)

    mydb.commit()
    cursor.close()
    mydb.close() 
