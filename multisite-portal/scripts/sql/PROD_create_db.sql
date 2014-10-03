CREATE DATABASE IF NOT EXISTS isobar_ca CHARACTER SET utf8;
CREATE DATABASE IF NOT EXISTS isobar_hu CHARACTER SET utf8;

use mysql;
INSERT INTO user (Host,User,Password) VALUES('localhost','isobar_ca',PASSWORD('zAVFxfGRy'));
INSERT INTO user (Host,User,Password) VALUES('localhost','isobar_hu',PASSWORD('P21R37kDP'));


flush privileges; 
grant SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER on isobar_ca.* to isobar_ca@localhost;
grant SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER on isobar_hu.* to isobar_hu@localhost;


flush privileges;