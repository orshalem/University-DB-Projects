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

    # Create the 'address' table to store address information
    cursor.execute("""
        CREATE TABLE address (
            address_id INT PRIMARY KEY,
            in_street INT NOT NULL,
            street_number SMALLINT NOT NULL,
            floor SMALLINT NOT NULL,
            FOREIGN KEY (in_street) REFERENCES street(street_id)
        );
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
