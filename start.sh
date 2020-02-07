#! /usr/bash

#CREATE TABLE `archives`(
#   `id` INT UNSIGNED AUTO_INCREMENT,
#   `province` VARCHAR(100),
#   `city` VARCHAR(100),
#   `publish_time` VARCHAR(100),
#   `publish_date` VARCHAR(100),
#   `title` VARCHAR(100),
#   `content` TEXT,
#   `link` VARCHAR(200),
#   `links_to_pic` VARCHAR(200),
#   `announce_type` VARCHAR(100),
#   PRIMARY KEY ( `id` )
#)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

read -p "Enter database password: " password
export PASSWORD=$password
(python3 ./app.py > /dev/null 2>&1 &)
