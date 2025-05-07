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

    # Create the 'meal_item' table that links meals to their items
    cursor.execute("""
        CREATE TABLE meal_item (
            meal_id INT,                           -- ID of the meal
            item_id INT NOT NULL,                  -- ID of the individual item
            PRIMARY KEY (meal_id, item_id),        -- Composite primary key
            FOREIGN KEY (meal_id) REFERENCES menu_meal(meal_id),   -- Foreign key to menu_meal
            FOREIGN KEY (item_id) REFERENCES menu_item(item_id)    -- Foreign key to menu_item
        );
    """)

    mydb.commit()
    cursor.close()
    mydb.close()
