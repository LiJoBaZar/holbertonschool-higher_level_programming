-- States Table
-- This SQL creates DataBAse and data states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(256));
