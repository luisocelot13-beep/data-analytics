pay_rate = float(input('Please type in pay rate:'))  # I used float becuase there a chance i may use decimal numbers
hours_worked = int(input('Please type in hours worked:'))

if hours_worked > 40:
    regular_pay = 40 * pay_rate

    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    total_pay = regular_pay + overtime_pay


else:
    total_pay = hours_worked * pay_rate
    
    
print(f'your total pay is {total_pay:.2f}')

annual_gross = total_pay * 52

print(f'Your annual gross pay is {annual_gross}')
