fruit_flavors = ('apple','kiwi','watermelon')

fruity_flavors = ('lemon','sunny','kite')

candy_combinations = set()

candy_combinations.add( fruit_flavors[0] + ' ' + fruity_flavors[0]) 
candy_combinations.add(fruit_flavors[1] + ' ' + fruity_flavors[1])
candy_combinations.add(fruit_flavors[2] + ' '  +  fruity_flavors [2])
print('Todays candy options include:')
print(candy_combinations)
# what i noticed immediately is that the output would change its patter im assuming set has to be the reason