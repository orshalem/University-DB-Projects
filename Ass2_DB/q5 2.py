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

    # Execute a SQL query to find:
    # (number of times the least-ordered meal was ordered)
    # minus
    # (number of times its items were ordered together but not as a meal)
    cursor.execute("""
        WITH meal_order_counts AS (
            -- Count how many times each meal was ordered (including 0)
            SELECT mm.meal_id, COUNT(oi.order_id) AS num_orders
            FROM menu_meal mm
            LEFT JOIN order_item oi 
                ON oi.item_id = mm.meal_id AND oi.is_meal = 1
            GROUP BY mm.meal_id
        ),

        min_orders AS (
            -- Find the minimum number of times any meal was ordered
            SELECT MIN(num_orders) AS min_order_count
            FROM meal_order_counts
        ),

        least_ordered_meals AS (
            -- Get the meal(s) with that minimum number of orders
            SELECT m.meal_id, m.num_orders
            FROM meal_order_counts m
            JOIN min_orders mo ON m.num_orders = mo.min_order_count
        ),

        items_ordered_separately AS (
            -- For those least-ordered meals, count how many times all their items were ordered together (not as a meal)
            SELECT lom.meal_id, COUNT(DISTINCT oi1.order_id) AS separate_orders
            FROM least_ordered_meals lom
            JOIN meal_item mi ON lom.meal_id = mi.meal_id
            JOIN order_item oi1 ON mi.item_id = oi1.item_id AND oi1.is_meal = 0
            WHERE NOT EXISTS (
                SELECT 1
                FROM meal_item mi2
                WHERE mi2.meal_id = lom.meal_id
                AND NOT EXISTS (
                    SELECT 1
                    FROM order_item oi2
                    WHERE oi2.order_id = oi1.order_id
                      AND oi2.item_id = mi2.item_id
                      AND oi2.is_meal = 0
                )
            )
            GROUP BY lom.meal_id
        )

        -- Final result: how many times the least-ordered meal was ordered
        -- minus how many times its items were ordered together (not as a meal)
        SELECT lom.num_orders - COALESCE(ios.separate_orders, 0) AS result
        FROM least_ordered_meals lom
        LEFT JOIN items_ordered_separately ios ON lom.meal_id = ios.meal_id;
    """)

    print(', '.join(str(row) for row in cursor.fetchall()))

  