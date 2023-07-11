-- Create the stored procedure
DELIMITER //

CREATE PROCEDURE ListTables(IN dbName VARCHAR(255))
BEGIN
  -- Declare variables
  DECLARE tableName VARCHAR(255);

  -- Create a temporary table to store the table names
  CREATE TEMPORARY TABLE IF NOT EXISTS temp_tables (table_name VARCHAR(255));

  -- Populate the temporary table with the table names
  SET @query = CONCAT('INSERT INTO temp_tables (table_name) SELECT table_name FROM information_schema.TABLES WHERE table_schema = ''', dbName, ''';');
  PREPARE stmt FROM @query;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;

  -- Select the table names from the temporary table
  SELECT table_name AS 'Table' FROM temp_tables;

  -- Drop the temporary table
  DROP TABLE IF EXISTS temp_tables;
END //

DELIMITER ;

