-- Retrieve the full description of the table 'first_table' in the 'hbtn_0c_0' database
SELECT column_name, column_type, is_nullable, column_default
FROM information_schema.COLUMNS
WHERE table_schema = 'hbtn_0c_0'
  AND table_name = 'first_table';

