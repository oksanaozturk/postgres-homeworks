-- SQL-команды для создания таблиц
CREATE TABLE customers_data (
	customer_id varchar(10) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
	contact_name varchar(50) NOT NULL
);


CREATE TABLE employees_data (
	employee_id integer PRIMARY KEY,
	first_name varchar(12) NOT NULL,
	last_name varchar(12) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE orders_data (
	order_id integer PRIMARY KEY,
	customer_id varchar REFERENCES customers_data(customer_id),
	employee_id integer REFERENCES employees_data(employee_id),
    order_date date NOT NULL,
	ship_city varchar(15) NOT NULL
);
