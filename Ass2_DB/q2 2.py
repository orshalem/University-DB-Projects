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

    # Create the 'menu_meal' table to store meal information
    cursor.execute("""
        CREATE TABLE menu_meal (
            meal_id INT PRIMARY KEY,           -- Unique identifier for each meal
            meal_name VARCHAR(255) NOT NULL,   -- Name of the meal
            price SMALLINT NOT NULL,           -- Price of the full meal
            served_at VARCHAR(255) NOT NULL    -- Location or time when the meal is served
        );
    """)


    mydb.commit()
    cursor.close()
    mydb.close()
