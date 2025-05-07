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

    # Update the 'meal_item' table with sample data
    cursor.execute("""
        INSERT INTO meal_item (meal_id, item_id)
        VALUES (1, 1), (1, 4), (1, 12),
        (2, 3), (2, 5), (2, 12),
        (3, 1), (3, 6), (3, 12),
        (4, 1), (4, 7), (4, 12),
        (5, 3), (5, 8), (5, 12),
        (6, 9), (6, 13),
        (7, 10), (7, 13),
        (8, 11), (8, 13);
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
