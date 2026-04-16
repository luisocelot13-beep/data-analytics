 /* 4a)The table products holds the items that they sell,price,supplier,category_id
 b) the table categories holds information category name, description,category id.*/
 select *
 from employees;
 /* 5a) Margaret peacock name is the closest sounding bird name in table.*/
 
 select *
 from products;
 
 /* 6a)77 records returned,by clicking on the drop down and selecting limit to 10 rows
 6b) you will use "limit" then the quantity of rows you'd like returned back ex
 select *
 from products
 limit 10 */
 
 select *
 from categories;
 /*7c) the seafood category id is '8'*/
 
 select OrderID,OrderDate,ShipName,ShipCountry
 from orders
 limit 50
 
 
 
 