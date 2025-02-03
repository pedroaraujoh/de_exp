create database oficial_db;

create schema my_schema;

create table oficial_db.my_schema.my_table (
	col1	varchar(100),
	col2	numeric(14,2)
);

insert into oficial_db.my_schema.my_table 
values (
	'alehandro', '15.2'
)

select * from oficial_db.my_schema.my_table