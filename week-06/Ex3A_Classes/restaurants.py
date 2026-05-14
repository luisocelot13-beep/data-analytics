class Restaurant:
    """Represents a resaurant and its food type."""
    def __init__(self,rest_name,food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f'{self.rest_name} serves {self.food_type}')

    def res_open(self):
        print(f'{self.rest_name} is open.')

rest_1 = Restaurant('Olive garden','Italian')
rest_2 = Restaurant('Burger king','Fast food')
rest_3 = Restaurant('Wendys','Fast food')


rest_1.describe_rest()
rest_1.res_open()
print()
rest_2.describe_rest()
rest_2.res_open()
print()
rest_3.describe_rest()
rest_3.res_open()