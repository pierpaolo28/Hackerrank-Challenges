# Weather Observation Station 19
SELECT ROUND(POW(POW(ABS(MAX(LAT_N)-MIN(LAT_N)),2) + POW(ABS(MAX(LONG_W)-MIN(LONG_W)),2),1/2),4)
FROM STATION;

# Weather Observation Station 20
SELECT  ROUND(LAT_N, 4)
FROM    Station AS S
WHERE (
        SELECT  COUNT(Lat_N)
        FROM    Station
        WHERE   Lat_N < S.Lat_N
) = (
        SELECT  COUNT(Lat_N)
        FROM    Station
        WHERE   Lat_N > S.Lat_N
)

# Revising Aggregations - The Count Function
SELECT COUNT(NAME)
FROM CITY
WHERE POPULATION > 100000

# Revising Aggregations - The Sum Function
SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'

# Revising Aggregations - Averages
SELECT AVG(POPULATION)
FROM CITY
WHERE DISTRICT = 'California'

# Average Population
SELECT ROUND(AVG(POPULATION))
FROM CITY

# Japan Population
SELECT SUM(POPULATION)
FROM CITY
WHERE COUNTRYCODE = 'JPN'

# Population Density Difference
SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY

# The Blunder
SELECT CEIL(AVG(SALARY)-AVG(REPLACE(SALARY,'0','')))
FROM EMPLOYEES;

# Top Earners
SELECT MONTHS * SALARY AS EARNINGS, COUNT(*)
FROM EMPLOYEE
GROUP BY EARNINGS DESC
LIMIT 1;

# Weather Observation Station 2
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2)
FROM STATION

# Weather Observation Station 13
SELECT TRUNCATE(SUM(LAT_N), 4)
  FROM STATION
 WHERE LAT_N BETWEEN 38.7880 AND 137.2345;

# Weather Observation Station 14
SELECT TRUNCATE(MAX(LAT_N), 4)
  FROM STATION
 WHERE LAT_N < 137.2345;

# Weather Observation Station 15
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1

# Weather Observation Station 16
SELECT ROUND(MIN(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7780

# Weather Observation Station 17
SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1

# Weather Observation Station 18
SELECT ROUND(MAX(LAT_N) - MIN(LAT_N) + MAX(LONG_W) - MIN(LONG_W), 4)
FROM STATION