CREATE DATABASE names;

\connect names;

CREATE TABLE name_freq(
  state TEXT,
  gender TEXT,
  year INT,
  name TEXT,
  freq INT
);

CREATE TABLE region(
  state TEXT,
  region TEXT
);

CREATE TABLE election(
  state TEXT,
  democrat INT,
  republican INT,
  other INT,
  year INT
);

CREATE TABLE candidate(
  year INT, 
  party TEXT,
  name TEXT
);

\copy name_freq FROM 'data/all_state_1950.csv' DELIMITER ',' CSV;
\copy election FROM 'data/election.csv' DELIMITER ',' CSV HEADER;
\copy candidate FROM 'data/candidates.csv' DELIMITER ',' CSV HEADER;
\copy region FROM 'data/regions.csv' DELIMITER ',' CSV;


