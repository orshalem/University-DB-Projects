# Import the MySQL connector library
import mysql.connector

# Main program execution starts here
if __name__ == '__main__':
    # Connect to the MySQL database using provided credentials and port
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )

    # Create a cursor object to interact with the database
    cursor = mydb.cursor()

    # Execute the SQL query to retrieve summarized data per nationality
    cursor.execute("""
              SELECT a.Nationality AS Country,          -- Country's nationality
               b.avg_pts AS AvgPoints,           -- Average points for drivers of that nationality
               a.min_time AS MinTime,           -- Minimum lap time (if available)
               c.latest AS LatestWinDate        -- Most recent race win date for that nationality
        FROM
          (
            -- Subquery “a”: Retrieve the minimum lap time for each nationality,
            -- ensuring that even nationalities with no fastest lap will appear.
            SELECT Nationality, MIN(Time) AS min_time
            FROM (
              -- Combining data from 'drivers' and 'fastest_laps' tables to fetch lap times.
              SELECT d.Nationality, f.Time
              FROM drivers d, fastest_laps f
              WHERE d.Driver = f.Driver
                AND f.Time <> ''                      -- Exclude invalid or empty lap times
              UNION
              -- Including nationalities with no recorded fastest lap time.
              SELECT Nationality, NULL AS Time
              FROM drivers
            ) AS combined_data
            GROUP BY Nationality
          ) AS a
        JOIN
          (
            -- Subquery “b”: Calculate the average points (PTS) for drivers grouped by nationality.
            SELECT Nationality, AVG(PTS) AS avg_pts
            FROM drivers
            GROUP BY Nationality
          ) AS b
        ON a.Nationality = b.Nationality
        
        JOIN
          (
            -- Subquery “c”: Get the latest race date for each nationality.
            -- Nationalities with no winner records are included with a NULL date.
            SELECT Nationality, MAX(Date) AS latest
            FROM (
              -- Combining data from 'drivers' and 'winners' to fetch race dates.
              SELECT d.Nationality, w.Date
              FROM winners w, drivers d
              WHERE d.Driver = w.Winner
              UNION
              -- Nationalities without a winner are included with NULL dates.
              SELECT Nationality, NULL AS Date
              FROM drivers
            ) AS race_data
            GROUP BY Nationality
          ) AS c
        ON a.Nationality = c.Nationality;
    """)

    # Fetch all the results and print them in a single line, comma-separated
    print(', '.join(str(row) for row in cursor.fetchall()))
