import mysql.connector

# This script finds how many races were won in 2001 by the team (Car)
# that had the most race wins in 1999.

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()

    # SQL Query: Counts races in 2001 won by the top-winning team from 1999
    cursor.execute("""
    SELECT COUNT(*) 
    FROM winners
    WHERE YEAR(Date) = 2001
      AND Car = (
        -- Subquery to find the Car (team) with the most wins in 1999
        SELECT Car
        FROM (
          SELECT Car, COUNT(*) AS total_wins_1999
          FROM winners
          WHERE YEAR(Date) = 1999
          GROUP BY Car
        ) AS top_teams_1999
        WHERE total_wins_1999 = (
          -- Get the maximum number of wins by any team in 1999
          SELECT MAX(total_wins_1999)
          FROM (
            SELECT Car, COUNT(*) AS total_wins_1999
            FROM winners
            WHERE YEAR(Date) = 1999
            GROUP BY Car
          ) AS all_team_wins_1999
        )
      );
    """)

    # Print the single numeric result
    print(', '.join(str(row) for row in cursor.fetchall()))
