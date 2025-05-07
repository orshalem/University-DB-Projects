import mysql.connector

# This script calculates the difference in total points 
# between the Ferrari and Maserati teams.

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()

    # SQL query to calculate difference in total points
    cursor.execute("""
    SELECT (SELECT SUM(PTS)
            FROM teams
            WHERE Team = 'Ferrari')
             -
           (SELECT SUM(PTS) 
            FROM teams 
            WHERE Team = 'Maserati') AS diff;
    """)

    # Print the single numeric result
    print(', '.join(str(row) for row in cursor.fetchall()))
