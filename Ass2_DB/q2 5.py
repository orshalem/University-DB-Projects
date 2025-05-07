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

    # Create the 'street' table to store street information
    cursor.execute("""
        CREATE TABLE street (
            street_id INT PRIMARY KEY,
            street_name VARCHAR(255) NOT NULL,
            in_city INT NOT NULL,
            FOREIGN KEY (in_city) REFERENCES city(city_id)
            );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
