
CREATE TABLE  publish_projectinfo_owner  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY, projectinfo_id  integer NOT NULL, user_id  integer NOT NULL) ;



CREATE TABLE  publish_projectinfo_second_approver  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  projectinfo_id  integer NOT NULL,  user_id  integer NOT NULL);



CREATE TABLE  publish_publishapprovalhistory  ( id  integer AUTO_INCREMENT NOT NULL PRIMARY KEY,  approve_count  varchar(32) NOT NULL,  approve_status  varchar(32) NOT NULL,  refuse_reason  longtext NULL,  first_approve_time  datetime(6) NULL,  second_approve_time  datetime(6) NULL,  first_approver_id  integer NULL);

