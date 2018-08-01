
CREATE TABLE  publish_approvallevel  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  name  varchar(32) NOT NULL);


CREATE TABLE  publish_approver  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  role  varchar(50) NULL,  approver_id  integer NOT NULL);


CREATE TABLE  publish_festival  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  name  varchar(32) NOT NULL,  start_day  date NOT NULL,  end_day  date NULL);


CREATE TABLE  publish_mailgroup  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  email  varchar(255) NOT NULL,  name  varchar(64) NULL);


CREATE TABLE  publish_projectinfo  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  creator_id  integer NULL,  group_id  integer NOT NULL);


CREATE TABLE  publish_projectinfo_first_approver  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  projectinfo_id  integer NOT NULL,  user_id  integer NOT NULL);



CREATE TABLE  publish_projectinfo_mail_group  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  projectinfo_id  integer NOT NULL,  mailgroup_id  integer NOT NULL);


