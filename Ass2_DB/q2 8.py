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

    # Create the 'full_order' table to store order information
    cursor.execute("""
        CREATE TABLE full_order (
            order_id INT PRIMARY KEY,
            order_time DATETIME NOT NULL,
            by_client INT NOT NULL,
            FOREIGN KEY (by_client) REFERENCES client(client_id)
        );
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
