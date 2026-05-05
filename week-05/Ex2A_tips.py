# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

#Calculate the unknown 
total_due = food_cost + tax + tip

#Display the results
#print('The total due is ' + str(total_due))  # the total due is 97.79

# the str() is converting the integer into a string value.
#print('Food cost is ' + str(food_cost) + ' and tax is ' + str(tax))

print('food cost is ' + str(food_cost) + 'and tax is ' + str(tax))
#print('Tip is ' + str(tip))
print('Total due is' + str(total_due))
print('Tip is ' + format(tip,'.2f'))