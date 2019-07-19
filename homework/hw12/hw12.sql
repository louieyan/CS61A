CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
  WHERE sizes.min < dogs.height AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT child FROM parents, dogs
  WHERE parents.parent = dogs.name
  ORDER BY height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS first, b.child AS second  
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Silibings that have same size
CREATE TABLE siblings_have_same_size AS
  SELECT a.first, a.second, b.size FROM siblings AS a, size_of_dogs AS b, size_of_dogs AS c
  WHERE a.first = b.name AND a.second = c.name AND b.size = c.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT a.first || " and " || a.second || " are " || a.size || " siblings"
  FROM siblings_have_same_size AS a;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT dogs.name, dogs.height, dogs.height FROM dogs
ORDER BY dogs.height;

INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT a.dogs || ", " || b.dogs, a.stack_height+b.stack_height, b.last_height
FROM stacks_helper AS a, stacks_helper AS b
WHERE a.last_height < b.last_height;



INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT a.dogs || ", " || b.dogs, a.stack_height+b.stack_height, b.last_height
FROM stacks_helper AS a, stacks_helper AS b
WHERE a.stack_height > a.last_height AND b.stack_height = b.last_height AND a.last_height < b.last_height;


INSERT INTO stacks_helper(dogs, stack_height, last_height)
SELECT a.dogs || ", " || b.dogs, a.stack_height+b.stack_height, b.last_height
FROM stacks_helper AS a, stacks_helper AS b
WHERE a.stack_height > 100 AND b.stack_height = b.last_height AND a.last_height < b.last_height;


-- SELECT * FROM stacks_helper; 



CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper
  WHERE stack_height >= 170;
