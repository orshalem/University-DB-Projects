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

    # Update the 'menu_meal' table with sample data
    cursor.execute("""
        INSERT INTO menu_meal (meal_id, meal_name, price, served_at)
        VALUES (1, 'small Oburger Meal', 8, 'all day'),
        (2, 'large Oburger Meal', 14, 'all day'),
        (3, 'chicken Oburger meal', 8, 'all day'),
        (4, 'small Onuggets meal', 7, 'all day'),
        (5, 'large Onuggets meal', 11, 'all day'),
        (6, 'Omfast', 4, 'morning'),
        (7, 'Opanfast', 4, 'morning'),
        (8, 'Owaffast', 4, 'morning');
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
