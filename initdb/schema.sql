
USE bosta_asses;

-- Creating the UserFact table
CREATE TABLE UserFact (
    user_id INT  PRIMARY KEY,
    gender VARCHAR(10),
    email VARCHAR(100),
    phone VARCHAR(20),
    cell VARCHAR(20),
    dob_date DATE,
    dob_age INT,
    registered_date DATE,
    registered_age INT,
    nationality VARCHAR(10)
);

-- Creating the NameDimension table
CREATE TABLE NameDimension (
    name_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(10),
    first VARCHAR(50),
    last VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES UserFact(user_id)
);

-- Creating the LocationDimension table
CREATE TABLE  LocationDimension (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    street_number INT,
    street_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postcode VARCHAR(50),
    coordinates_latitude DECIMAL(9, 6),
    coordinates_longitude DECIMAL(9, 6),
    timezone_offset VARCHAR(10),
    timezone_description VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES UserFact(user_id)
);

-- Creating the LoginDimension table
CREATE TABLE LoginDimension (
    login_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    uuid VARCHAR(36),
    username VARCHAR(50),
    password VARCHAR(100),
    salt VARCHAR(50),
    md5 VARCHAR(32),
    sha1 VARCHAR(40),
    sha256 VARCHAR(64),
    FOREIGN KEY (user_id) REFERENCES UserFact(user_id)
);

-- Creating the InfoDimension table
CREATE TABLE InfoDimension (
    info_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    seed VARCHAR(50),
    version VARCHAR(10),
    FOREIGN KEY (user_id) REFERENCES UserFact(user_id)
);

-- Creating the PictureDimension table
CREATE TABLE PictureDimension (
    picture_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    picture_large VARCHAR(255),
    picture_medium VARCHAR(255),
    picture_thumbnail VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES UserFact(user_id)
);