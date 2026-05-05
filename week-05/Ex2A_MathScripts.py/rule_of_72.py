# Rule of 72
savings = 10000
interest = 0.06
years = 72 / interest

#calculated double
 
double_amount = savings * 2

print('Your current savings is ' + str(savings) )
print ('At a ' + format(interest,'.0%') + '  interest rate, your savings account will be worth ' + format(double_amount,'.2f') + ' in ' + format(years,'.1f'))