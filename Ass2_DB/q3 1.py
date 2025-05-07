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

    # Update the 'menu_item' table with sample data
    cursor.execute("""
        INSERT INTO menu_item (item_id, item_name, price)
        VALUES (1, 'small fries', 2),
        (2, 'Osalad', 2), 
        (3, 'large fries', 5), 
        (4, 'Oburger', 6),
        (5, 'double Oburger', 10), 
        (6, 'chicken Oburger', 3), 
        (7, 'Onuggets', 3),
        (8, 'double Onuggets', 5), 
        (9, 'Omlette', 3), 
        (10, 'Opancake', 3), 
        (11, 'Owaffle', 3),
        (12, 'light Obeverage', 2), 
        (13, 'hot Obeverage', 2);
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
