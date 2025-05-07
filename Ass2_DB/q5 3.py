import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgers",
        port=3307
    )

    cursor = mydb.cursor()

    # Execute an SQL query to retrieve meal names
    # where the meal's price is greater than or equal to the sum of its individual items' prices
    cursor.execute("""
        SELECT menu_meal.meal_name
        FROM menu_meal
        JOIN meal_item ON menu_meal.meal_id = meal_item.meal_id
        JOIN menu_item ON meal_item.item_id = menu_item.item_id
        GROUP BY menu_meal.meal_id, menu_meal.meal_name, menu_meal.price
        HAVING menu_meal.price >= SUM(menu_item.price);
    """)


    print(', '.join(str(row) for row in cursor.fetchall()))

  