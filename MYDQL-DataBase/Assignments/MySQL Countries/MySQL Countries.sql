USE world;

SELECT c.Name AS Country, cl.Language, cl.Percentage
FROM countrylanguage cl
JOIN country c ON cl.CountryCode = c.Code
WHERE cl.Language = 'Slovene'
ORDER BY cl.Percentage DESC;


SELECT c.Name AS Country, COUNT(ci.ID) AS TotalCities
FROM city ci
JOIN country c ON ci.CountryCode = c.Code
GROUP BY c.Name
ORDER BY TotalCities DESC;


SELECT Name AS City, Population
FROM city
WHERE CountryCode = 'MEX' AND Population > 500000
ORDER BY Population DESC;


SELECT c.Name AS Country, cl.Language, cl.Percentage
FROM countrylanguage cl
JOIN country c ON cl.CountryCode = c.Code
WHERE cl.Percentage > 89
ORDER BY cl.Percentage DESC;


SELECT Name, SurfaceArea, Population
FROM country
WHERE SurfaceArea < 501 AND Population > 100000;


SELECT Name, GovernmentForm, Capital, LifeExpectancy
FROM country
WHERE GovernmentForm = 'Constitutional Monarchy'
  AND Capital > 200
  AND LifeExpectancy > 75;


SELECT c.Name AS Country, ci.Name AS City, ci.District, ci.Population
FROM city ci
JOIN country c ON ci.CountryCode = c.Code
WHERE c.Name = 'Argentina'
  AND ci.District = 'Buenos Aires'
  AND ci.Population > 500000;


SELECT Region, COUNT(*) AS NumberOfCountries
FROM country
GROUP BY Region
ORDER BY NumberOfCountries DESC;