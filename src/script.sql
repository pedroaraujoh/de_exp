-- Active: 1738546239605@@localhost@5432@db
-- create database db;

create schema schema1;

create table db.schema1.table1 (
	col1	varchar(100),
	col2	numeric(14,2)
);

insert into db.schema1.table1 
values 
	('maria', 22.5),
	('jose', 18.75),
	('ana', 33.2),
	('pedro', 45.8)

select * from db.schema1.table1;
select count(*) from db.schema1.table1