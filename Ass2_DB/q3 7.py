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

    # Update the 'client' table with sample data
    cursor.execute("""
        INSERT INTO client (client_id, client_name, client_address)
        VALUES (1, 'Lee Kang', 5),
            (2, 'Wang Fu', 6),
            (3, 'Sandro Moretti', 3),
            (4, 'Giuseppe Angelo', 4),
            (5, 'Favian Adames Alonso', 1),
            (6, 'Edward Pagan Henriquez', 2);
    """)
    mydb.commit()
    cursor.close()
    mydb.close()
