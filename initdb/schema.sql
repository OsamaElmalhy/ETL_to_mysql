USE bosta_asses;

-- Create users table
CREATE TABLE users (
    gender VARCHAR(10),
    title VARCHAR(10),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    user_id VARCHAR(36) PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    salt VARCHAR(50),
    md5 CHAR(32),
    sha1 CHAR(40),
    sha256 CHAR(64),
    dob DATE,
    dob_age INT,
    registered DATE,
    registered_age INT,
    phone VARCHAR(20),
    cell VARCHAR(20),
    id_name VARCHAR(50),
    id_value VARCHAR(50),
    nat CHAR(2)
);

-- Create locations table
CREATE TABLE locations (
    user_id VARCHAR(36),
    street_number INT,
    street_name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postcode VARCHAR(255),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    timezone_offset VARCHAR(10),
    timezone_description VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create pictures table
CREATE TABLE pictures (
	user_id VARCHAR(36),
    large_url VARCHAR(255),
    medium_url VARCHAR(255),
    thumbnail_url VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
