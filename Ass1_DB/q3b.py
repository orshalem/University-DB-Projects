import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
        SELECT fl.Driver, MIN(fl.Time) AS min_time
        FROM fastest_laps fl
        JOIN (
            SELECT Winner, SUM(Laps) AS total_laps
            FROM winners
            WHERE YEAR(Date) = 2000
            GROUP BY Winner
        ) AS laps_per_driver
        ON fl.Driver = laps_per_driver.Winner
        JOIN (
            SELECT Winner
            FROM winners
            WHERE YEAR(Date) = 2000
            GROUP BY Winner
            ORDER BY SUM(Laps) DESC
        ) AS max_laps_driver
        ON laps_per_driver.Winner = max_laps_driver.Winner
        WHERE laps_per_driver.total_laps = (
            SELECT MAX(total_laps)
            FROM (
                SELECT SUM(Laps) AS total_laps
                FROM winners
                WHERE YEAR(Date) = 2000
                GROUP BY Winner
            ) AS laps_per_driver_subquery
        )
        GROUP BY fl.Driver;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
