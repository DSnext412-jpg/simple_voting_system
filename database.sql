CREATE DATABASE IF NOT EXISTS voting_db;



USE voting_db;



CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    has_voted BOOLEAN DEFAULT FALSE
);



CREATE TABLE IF NOT EXISTS candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    party VARCHAR(255) NOT NULL,
    symbol VARCHAR(255)
);



CREATE TABLE IF NOT EXISTS votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    candidate_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(id)
);



INSERT INTO candidates (name, party, symbol) VALUES
('BJP', '6 C', 'LOTUS'),
('shivsena', '2 C', 'Flaming Torch'),
('Navnirman Sena', '1 C', 'Railway Engine');



INSERT INTO users (email, password) VALUES ('test@example.com', 'password');
