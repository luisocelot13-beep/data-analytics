fav_food = [ 'tacos','pizza','burgers','sushi','hot dogs']

for number, food in enumerate(reversed(fav_food),start=1):
    if number == 1:
        print(f'{number} {food} <-- top pick')

    else:
        print(number,food)