-- For creates the Table 'force_name' on my MySQL server
-- The description is id("INT") name("VARCHAR(256)") can't be NULL.
CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
