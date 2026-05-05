# tip amount
bill = int(input('Type your bill amount:'))
tip_percent = 0.20

tip = bill * tip_percent

total_bill = tip + bill

print ('The Tip on a $' + str(bill)  + ' resturant bill is $' + format(tip,'.2f'))

#introducing the input function to tip amount 
# the possible pit falls i can see is mabye customer might write out the number and it might be issues when python runs it