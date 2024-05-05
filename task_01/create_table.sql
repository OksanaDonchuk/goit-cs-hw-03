CREATE TABLE IF NOT exists users (
id SERIAL PRIMARY KEY,
fullname VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT exists status (
id SERIAL PRIMARY KEY,
name VARCHAR(50) UNIQUE NOT null check (name in ('new', 'in progress', 'completed'))
);

CREATE TABLE IF NOT exists tasks (
id SERIAL PRIMARY KEY,
title VARCHAR(100) NOT NULL,
description text,
status_id INT,
user_id INT,
FOREIGN KEY (status_id) REFERENCES status(id),
FOREIGN KEY (user_id) references users(id)
ON DELETE cascade
ON UPDATE CASCADE
);