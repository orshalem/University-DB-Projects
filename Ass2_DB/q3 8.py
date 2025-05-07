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

    # Update the 'full_order' table with sample data
    cursor.execute("""
        INSERT INTO full_order (order_id, order_time, by_client)
        VALUES (1, '2025-04-20 08:15:00', 1),
        (2, '2025-04-20 09:00:00', 1),
        (3, '2025-04-20 10:00:00', 2),
        (4, '2025-04-20 11:00:00', 2),
        (5, '2025-04-20 13:00:00', 1),
        (6, '2025-04-20 08:30:00', 3),
        (7, '2025-04-20 14:00:00', 3),
        (8, '2025-04-20 14:30:00', 4),
        (9, '2025-04-20 12:00:00', 5),
        (10, '2025-04-20 12:15:00', 6),
        (11, '2025-04-20 08:15:00', 5);
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
