import mysql.connector

# This script computes the average points per car (team),
# but only for cars where a driver recorded a fastest lap under 120 seconds.
# It joins the 'drivers' and 'fastest_laps' tables using the Driver column,
# converts the Time field into total seconds, filters it, and averages PTS per car.

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
SELECT Car, AVG(PTS) AS avg_pts
FROM drivers
WHERE Car IN (
    SELECT DISTINCT Car
    FROM fastest_laps
    WHERE 
        MINUTE(STR_TO_DATE(Time, '%i:%s.%f')) * 60 +
        SECOND(STR_TO_DATE(Time, '%i:%s.%f')) +
        MICROSECOND(STR_TO_DATE(Time, '%i:%s.%f')) / 1000000 < 120
)
GROUP BY Car
ORDER BY avg_pts DESC;
    """)
    
    print(', '.join(str(row) for row in cursor.fetchall()))
