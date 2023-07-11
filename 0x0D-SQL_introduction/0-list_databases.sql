-- This script lists all databases on the MySQL server

-- Select the 'schema_name' column from the 'information_schema.SCHEMATA' table
-- 'schema_name' column contains the names of all databases
SELECT schema_name AS "Database"
FROM information_schema.SCHEMATA;

