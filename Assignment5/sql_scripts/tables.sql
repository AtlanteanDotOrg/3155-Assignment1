-- resources Table:
CREATE TABLE IF NOT EXISTS resources (
    id int NOT NULL AUTO_INCREMENT,
    item varchar(50) NOT NULL,
    amount int NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO resources(id, item, amount) VALUES 
	(1, 'bread', 12),
    (2, 'ham', 18),
    (3, 'cheese', 24);

SELECT * FROM resources;

-- sandwiches table:
CREATE TABLE IF NOT EXISTS sandwiches (
	id int NOT NULL AUTO_INCREMENT,
    sandwich_size varchar(50) NOT NULL,
    price decimal(5, 2) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO sandwiches(id, sandwich_size, price) VALUES
	(1, 'small', 1.75),
    (2, 'medium', 3.25),
    (3, 'large', 5.50);
    
SELECT * FROM sandwiches;