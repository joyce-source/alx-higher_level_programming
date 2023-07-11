-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_test_db_0;

-- Use the newly created database
USE hbtn_test_db_0;

-- Create three tables
CREATE TABLE IF NOT EXISTS holbteron_0 (id INT, name VARCHAR(255));
CREATE TABLE IF NOT EXISTS holbteron_1 (id INT, name VARCHAR(255));
CREATE TABLE IF NOT EXISTS holbteron_2 (id INT, name VARCHAR(255));

-- Retrieve the table names
SELECT table_name
FROM information_schema.TABLES
WHERE table_schema = 'hbtn_test_db_0';

