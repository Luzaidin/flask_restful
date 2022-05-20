docker exec -it {containerName} bash
mysql -u root -p
create database {databaseName};
use {databaseName};
create table user(_id INT  AUTO_INCREMENT, name VARCHAR(40), email VARCHAR(30), PRIMARY KEY (_id));
insert into user(name, email) values('Luis', 'Luis@Luis');
