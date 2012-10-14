/* Create main table */

CREATE DATABASE IF NOT EXISTS movie_users;

USE movie_users;

CREATE TABLE IF NOT EXISTS `users` (
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`name` varchar(128) NOT NULL,
	`movetitle` varchar(128) NOT NULL,
	`releasedate` date NOT NULL,
	`email` varchar(128),
	`phone` varchar(10)
);
