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

    # Execute an SQL query to retrieve meal names and how many times each meal was sold
    cursor.execute("""
          SELECT 
            menu_meal.meal_name,                        -- Meal name
            COUNT(order_item.order_id) AS total_sold    -- Count of times the meal was ordered
        FROM 
            menu_meal
        LEFT JOIN order_item 
            ON order_item.item_id = menu_meal.meal_id 
            AND order_item.is_meal = 1                  -- Only include rows where it was ordered as a meal
        GROUP BY 
            menu_meal.meal_id, menu_meal.meal_name
        ORDER BY 
            total_sold DESC;                            -- Sort from most sold to least
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))

  