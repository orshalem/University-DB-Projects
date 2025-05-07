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

    # Execute a SQL query to analyze meal type popularity by city
    # The query returns, for each city:
    # - Number of breakfast meals ordered (served_at = 'morning')
    # - Number of regular meals ordered (served_at = 'all day')
    #
    # Logic:
    # - Join city → street → address → client → full_order → order_item → menu_meal
    # - Only count rows where the order_item is a meal (is_meal = 1)
    # - Use SUM(boolean expression) to count matching values efficiently
    # - Group results by city name and sort alphabetically
    cursor.execute("""
        SELECT 
            city_name,
            SUM(menu_meal.served_at = 'morning') AS breakfast_count,
            SUM(menu_meal.served_at = 'all day') AS regular_count
        FROM 
            city
            JOIN street ON city.city_id = street.in_city
            JOIN address ON street.street_id = address.in_street
            JOIN client ON address.address_id = client.client_address
            JOIN full_order ON client.client_id = full_order.by_client
            JOIN order_item ON full_order.order_id = order_item.order_id
            JOIN menu_meal ON order_item.item_id = menu_meal.meal_id
        WHERE order_item.is_meal = 1
        GROUP BY city_name
        ORDER BY city_name ASC
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
