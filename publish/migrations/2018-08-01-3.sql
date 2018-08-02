

CREATE TABLE  publish_publishsheet  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  publish_date  varchar(32) NOT NULL,  publish_time  varchar(32) NOT NULL,  tapd_url  longtext NOT NULL,  sql_before  longtext NULL,  sql_after  longtext NULL,  consul_key  longtext NULL,  status  varchar(32) NOT NULL,  comment  longtext NULL,  reason  longtext NULL,  if_review  varchar(32) NOT NULL,  if_browse  varchar(32) NOT NULL,  if_order  varchar(32) NOT NULL,  if_buy  varchar(32) NOT NULL,  if_publish_ok  varchar(32) NOT NULL,  publish_result  longtext NULL,  approval_level_id  integer NULL,  creator_id  integer NOT NULL);


CREATE TABLE  publish_publishsheet_first_approver  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  publishsheet_id  integer NOT NULL,  user_id  integer NOT NULL);


CREATE TABLE  publish_publishsheet_goservices  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  publishsheet_id  integer NOT NULL,  goservices_id  integer NOT NULL);


CREATE TABLE  publish_publishsheet_qa  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  publishsheet_id  integer NOT NULL,  user_id  integer NOT NULL);


CREATE TABLE  publish_publishsheet_reviewer  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  publishsheet_id  integer NOT NULL,  user_id  integer NOT NULL);


CREATE TABLE  publish_publishsheet_second_approver  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  publishsheet_id  integer NOT NULL,  user_id  integer NOT NULL);


CREATE TABLE  publish_timeslotlevel  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  is_global  varchar(32) NOT NULL,  start_of_week  varchar(32) NOT NULL,  end_of_week  varchar(32) NOT NULL,  start_time  varchar(32) NULL,  end_time  varchar(32) NULL,  approval_level_id  integer NOT NULL,  creator_id  integer NULL);


CREATE TABLE  publish_projectinfo_timeslot_level  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  projectinfo_id  integer NOT NULL,  timeslotlevel_id  integer NOT NULL);

