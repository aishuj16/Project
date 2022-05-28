drop database if exists Library;
create database if not exists Library;
use Library ; 

create table lib(Member varchar(50), PRN varchar(50) primary key , ID varchar(50) Unique key ,
Firstname varchar(50) , Lastname  varchar(50) ,Address1  varchar(50) ,Address2  varchar(50) ,
postcode  varchar(50) , Mobile  varchar(50) , Bookid  varchar(50) ,Booktitle  varchar(50) ,Author varchar(50) ,
Borroweddate  varchar(50) ,Duedate  varchar(50) ,Dayonbook  varchar(50) ,Latereturnfine  varchar(50) ,
Dateoverdue  varchar(50) ,Actualprice  varchar(50))




