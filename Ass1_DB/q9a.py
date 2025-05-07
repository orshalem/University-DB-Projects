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
SELECT a.Nationality AS Nationality,
       b.avg_pts,
       a.min_time,
       c.latest
FROM
  (
    -- Subquery “a”: Get the minimum Time for each Nationality,
    -- making sure that every nationality appears even if there’s no fastest lap.
    SELECT Nationality, MIN(Time) AS min_time
    FROM (
      SELECT d.Nationality, f.Time
      FROM drivers d, fastest_laps f
      WHERE d.Driver = f.Driver
        AND f.Time <> ''
      UNION
      SELECT Nationality, NULL AS Time
      FROM drivers
    ) AS t1
    GROUP BY Nationality
  ) AS a,
  (
    -- Subquery “b”: Average PTS per Nationality (from drivers)
    SELECT Nationality, AVG(PTS) AS avg_pts
    FROM drivers
    GROUP BY Nationality
  ) AS b,
  (
    -- Subquery “c”: Get the maximum Date (latest) for each Nationality,
    -- making sure every nationality appears even if there’s no winner record.
    SELECT Nationality, MAX(Date) AS latest
    FROM (
      SELECT d.Nationality, w.Date
      FROM winners w, drivers d
      WHERE d.Driver = w.Winner
      UNION
      SELECT Nationality, NULL AS Date
      FROM drivers
    ) AS t2
    GROUP BY Nationality
  ) AS c
WHERE a.Nationality = b.Nationality
  AND b.Nationality = c.Nationality;



 """)
 print(', '.join(str(row) for row in cursor.fetchall()))