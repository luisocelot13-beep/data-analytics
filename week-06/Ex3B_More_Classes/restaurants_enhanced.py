class Restaurant:
    """Represents a resaurant and its food type."""
    def __init__(self,rest_name,food_type):
        self.rest_name = rest_name
        self.food_type = food_type

        self.number_served = 0
        self.customer_rating = []

    def add_num_served(self):
        customers = int(input('How many customers served today?'))
        self.number_served += customers

    def print_num_served(self):
        print(f'{self.rest_name} has served {self.number_served} customers')
    
    def customer_ratings(self):
       while True:
        rating = int(input('How would you rate your expierence from 1 to 5 (5 being excellent)'))
        if rating >= 1 and rating <= 5:
            self.customer_rating.append(rating)
            avg_rating = sum(self.customer_rating) / len(self.customer_rating)
            print(f'Your rating was {rating}.the average rating for this resaurant is {avg_rating}')

            break

        else:
            print('Sorry please enter a whole number between 1 and 5')


        avg_rating = sum(self.customer_rating) / len(self.customer_rating)
        print(f'Your rating was {rating}.The average rating for this restaurant is {avg_rating}.')

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def res_open(self):
        print(f'{self.rest_name} is open.')

rest_1 = Restaurant('Olive garden','Italian')
rest_1.describe_rest()
rest_1.add_num_served()
rest_1.print_num_served()
rest_1.customer_ratings()
rest_1.describe_rest()
rest_1.res_open()



