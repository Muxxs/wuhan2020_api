#! /usr/bash

#CREATE TABLE `archives`(
#   `id` INT UNSIGNED AUTO_INCREMENT,
#   `province` VARCHAR(255),
#   `city` VARCHAR(255),
#   `publish_time` VARCHAR(255),
#   `publish_date` VARCHAR(255),
#   `title` VARCHAR(255),
#   `content` TEXT,
#   `link` TEXT,
#   `links_to_pic` TEXT,
#   `announce_type` VARCHAR(100),
#   PRIMARY KEY ( `id` )
#)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

read -p "Enter database password: " password
export PASSWORD=$password
(python3 ./app.py > log.txt 2>&1 &)
