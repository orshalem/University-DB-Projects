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

    # Update the 'order_item' table with sample data
    cursor.execute("""
        INSERT INTO order_item (order_id, item_id, is_meal)
        VALUES (1, 6, 1),
        (2, 7, 1),
        (3, 8, 1),
        (4, 6, 1),
        (5, 1, 1),
        (6, 6, 0),
        (6, 12, 0),
        (6, 1, 0),
        (6, 6, 1),
        (7, 1, 0),
        (7, 1, 1),
        (8, 3, 0),
        (8, 2, 1),
        (9, 6, 1),
        (9, 4, 1),
        (9, 5, 1),
        (10, 2, 0),
        (10, 2, 1),
        (11, 1, 1);
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
