pay_rate = float(input('Please type in pay rate:'))  # I used float becuase there a chance i may use decimal numbers
hours_worked = int(input('Please type in hours worked:'))

if hours_worked > 40:
    regular_pay = 40 * pay_rate

    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)

    total_pay = regular_pay + overtime_pay

else:
    total_pay = hours_worked * pay_rate
    



annualgross_pay = total_pay * 52  

# annual gross pay

filing_status = input('Type single or joint status:')
#Filing status 


#Determine the tax rate
if filing_status == 'single':
    if annualgross_pay < 12000:
        tax_rate = 0.05
    elif annualgross_pay < 25000:
        tax_rate= 0.10
    elif annualgross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == 'joint':

    if annualgross_pay < 12000:
        tax_rate = 0.00
    elif annualgross_pay < 25000:
        tax_rate = 0.06
    elif annualgross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

tax_withheld = total_pay * tax_rate

net_pay = total_pay - tax_withheld

print(f'You worked this many hours per week {hours_worked}')
print(f'Because you earned {pay_rate} per hour, your gross weekly pay is {total_pay}')

print(f'Your filing status is {filing_status}')
print(f'Your tax withholding for the week is {tax_withheld:.2f}')
print(f'your 40net pay: $ {net_pay:.2f}')
