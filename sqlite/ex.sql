CREATE TABLE cities AS
  SELECT 38 AS latitude, 122 AS longitude, "Berkeley" AS name UNION
  SELECT 42,              71,              "Cambridge"        UNION
  SELECT 45,              93,              "Minneapolis"      UNION
  SELECT 33,             117,              "San Diego"        UNION
  SELECT 26,              80,              "Miami"            UNION
  SELECT 90,               0,              "North Pole";

CREATE TABLE cold AS
  SELECT name FROM cities WHERE latitude >= 43;

CREATE TABLE distance AS
  SELECT a.name AS first, b.name AS second,
  60*(b.latitude - a.latitude) AS distance 
  FROM cities AS a, cities AS b;

CREATE TABLE nouns AS
  SELECT "dog" AS phrase UNION
  SELECT "cat"           UNION
  SELECT "bird";

SELECT subject.phrase || " chased " || object.phrase
  FROM nouns AS subject, nouns AS object
  WHERE subject.phrase <> object.phrase;

CREATE TABLE ands AS
  SELECT phrase FROM nouns UNION
  SELECT first.phrase || " and " || second.phrase AS phrase
  FROM nouns AS first, nouns AS second
  WHERE first.phrase <> second.phrase;


SELECT subject.phrase || " chased " || object.phrase
  FROM ands AS subject, ands AS object
  WHERE subject.phrase <> object.phrase;


CREATE TABLE animals AS
  SELECT "dog" AS kind, 4 AS legs, 20 AS weight UNION
  SELECT "cat"        , 4        , 10           UNION
  SELECT "ferret"     , 4        , 10           UNION
  SELECT "parrot"     , 2        , 6            UNION
  SELECT "penguin"    , 2        , 10           UNION
  SELECT "t-rex"      , 2        , 12000; 