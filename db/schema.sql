-- Database Schema (Star Schema)

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    date DATE,
    status VARCHAR(50),
    customer VARCHAR(255),
    customer_type VARCHAR(50),
    products TEXT,
    item_sold INT,
    net_sales DECIMAL(10,2)
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_type VARCHAR(50)
);


