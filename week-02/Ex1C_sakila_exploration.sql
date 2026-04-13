/*
a) actor_id, first_name,last_name. All the information listed in this column is related to the actor info.
b) The film table has many columns listed the main take away for all this is related to film for example title,length,rating,rental_rate etc.
c) film_actor
d) Its very easy to read because the columns are seperated and labeled properly. The only thing I would change is mabye moving all the dates to the end.
e)Simple clean and not over cluttered.
f) Based on what you have learned so far, which tables do you need to use in order to
understand the names of all films that were rented on a specific date? Rental, film . How are
these tables related to each other? Answer with an explanation in full sentences. All of these tables are related by either a foreign key or primary key. Majority of them have inventory_id,film_id etc, they're linked to the main product which is films,actors in the film,customers rentals.
*/

select *
from rental;
select *
from film
