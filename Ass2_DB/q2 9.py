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

    # Create the 'order_item' table to store order items
    cursor.execute("""
        CREATE TABLE order_item (
            order_id INT,
            item_id INT,
            is_meal BOOLEAN,
            PRIMARY KEY (order_id, item_id, is_meal),
            FOREIGN KEY (order_id) REFERENCES full_order(order_id),
            FOREIGN KEY (item_id) REFERENCES menu_item(item_id)
            );
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
