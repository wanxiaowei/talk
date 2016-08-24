CREATE DATABASE IF NOT EXISTS talk;
USE talk;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS permission;
CREATE TABLE user (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                   name VARCHAR(100) NOT NULL,
                   password VARCHAR(100) NOT NULL,
                   permission_level INTEGER NOT NULL DEFAULT 3);
CREATE TABLE permission(level INTEGER NOT NULL,
                        context VARCHAR(100) NOT NULL);
INSERT INTO permission VALUES (1,'administer'),(2,'boss'),(3,'human being');
INSERT INTO user (name, password, permission_level) VALUES ('wanxiaowei', 'admin', 1)
