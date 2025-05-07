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

    # Update the 'raw_cost' column in the 'menu_meal' table for meal_id = 4
    # - The value is calculated as the sum of the prices of all items in the meal
    # - 'meal_item' defines which items are part of the meal
    # - 'menu_item' contains the prices of the individual items
    cursor.execute("""
        UPDATE menu_meal
        SET raw_cost = (
        SELECT SUM(menu_item.price)
        FROM meal_item
        JOIN menu_item ON meal_item.item_id = menu_item.item_id
        WHERE meal_item.meal_id = 4
        ) 
        WHERE meal_id = 4;
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
