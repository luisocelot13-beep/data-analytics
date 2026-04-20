/*1)Write a query to list the product id, product name, and unit price of every product that
Northwind sells.*/
SELECT ProductID,ProductName,UnitPrice
FROM products;
/*2) Write a query to identify the products where the unit price is $7.50 or less.*/
select *
from products
where UnitPrice <= 7.50;
/*3.)What are the products that we carry where we have no units on hand, but 1 or more
units are on backorder? */
select ProductID,ProductName,UnitsInStock,UnitsOnOrder
FROM products
where UnitsInStock = 0 and UnitsOnOrder >= 1;

/*Examine the products table. How does it identify the type (category) of each item
sold?*/
select ProductName,CategoryID
from products;

/*Where can you find a list of all categories? */
SELECT * FROM northwind.categories;

/*Write a set of queries to answer these
questions, ending with a query that creates a list of all the seafood items we carry*/

select *
from categories
where CategoryName = "Seafood";

/*5. Examine the products table again. How do you know what supplier each product
comes from? */
select SupplierID
from products;

/*Where can you find info on suppliers? */
SELECT * FROM northwind.suppliers;

/*Write a set of queries to find the
specific identifier for "Tokyo Traders" and then find all products from that supplier.*/
select *
from suppliers
where CompanyName = "Tokyo Traders";

select *
from products
where SupplierID = 4;



/*6. How many employees work at northwind? What employees have "manager"
somewhere in their job title? Write queries to answer each question.*/