import mysql.connector


# This script finds all pairs of Grand Prix events that had
# the same number of laps (more than 120), ensuring unique
# alphabetical order pairs like <Apple, Banana> not <Banana, Apple>.

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()

    # SQL query to get GP pairs with same laps > 120, alphabetical order only
    cursor.execute("""
    SELECT 
        a.`Grand Prix` AS GP1, 
        b.`Grand Prix` AS GP2, 
        a.Laps AS Laps
    FROM 
        winners AS a, winners AS b
    WHERE 
        a.Laps = b.Laps
        AND a.`Grand Prix` < b.`Grand Prix`
        AND a.Laps > 120
    ORDER BY 
        GP1, GP2;
    """)
   
    print(', '.join(str(row) for row in cursor.fetchall()))
