-- Let's create the table
CREATE TABLE customers (
    id serial PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT
);

-- Let's alter its replica identity for deletes/updates
ALTER TABLE customers REPLICA IDENTITY FULL;
