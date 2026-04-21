 /*1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.*/
select min(UnitPrice)
from products;

select ProductName,UnitPrice
from products
where UnitPrice = '2.5000';

/*2. Write a query to find the average price of all items that Northwind sells.
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
using the ROUND function to round the average price to the nearest cent.)*/
select round(avg(UnitPrice),2)
from  products;

/*3. Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.*/
select max(UnitPrice)
from products;

select p.ProductName,p.UnitPrice,s.CompanyName
from products as p
join suppliers as s
on p.SupplierID = s.SupplierID
where p.UnitPrice = '263.5000';

/*4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries).*/
select sum(Salary)
from employees;

/*5. Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)*/

select max(Salary) as mostmoney, min(Salary) as leastmoney
from employees;

/*6. Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here.*/

select s.SupplierID,s.CompanyName,count(p.SupplierID)
from suppliers as s
join products as p
on s.SupplierID = p.SupplierID
group by s.SupplierID,s.CompanyName
order by s.SupplierID;

/*7. Write a query to find the list of all category names and the average price for items in
each category.*/
select c.CategoryName,avg(p.UnitPrice)
from categories as c
join products as p
on c.CategoryID = p.CategoryID
group by c.CategoryName;
/*8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.*/

select s.supplierID,s.CompanyName,count(p.SupplierID) as count_iten
from suppliers as s
join products as p
on s.SupplierID = p.SupplierID
group by s.SupplierID, s.CompanyName
having count_iten >= 5;

/*9. Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list*/

select ProductID,ProductName,UnitPrice * UnitsInStock as inventory_value
from products
where UnitsInStock >= 1
order by inventory_value desc,ProductName asc;