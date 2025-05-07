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

    # Create the 'client' table to store client information
    cursor.execute("""
        CREATE TABLE client (
            client_id INT PRIMARY KEY,
            client_name VARCHAR(255) NOT NULL,
            client_address INT NOT NULL,
            FOREIGN KEY (client_address) REFERENCES address(address_id)
        );
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
