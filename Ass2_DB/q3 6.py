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

    # Update the 'address' table with sample data
    cursor.execute("""
        INSERT INTO address (address_id, in_street, street_number, floor)
        VALUES (1, 2, 10, 2),
        (2, 1, 1, 10),
        (3, 3, 23, 101),
        (4, 4, 52, 304),
        (5, 5, 5, 2),
        (6, 6, 34, 1);
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
