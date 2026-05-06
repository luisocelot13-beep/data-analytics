# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost
# $250 per day to rent (including the driver’s pay). How many vans do you need? How
# much will it cost to rent vans? What is the cost if you split it per person?
import math
people = 38
charter_seats = 15
cost = 250

vans_needed = math.ceil(people / charter_seats)

total_cost = vans_needed * cost

cost_per_person = total_cost / people
print(f'vans needed {vans_needed}')
print(f'total cost {total_cost}')
print(f'cost per person { cost_per_person:.2f}')

#A.) 19.74
#B.) 750.12
#C.) 750 for the vans
#D.)  Rounding issues 