sales_data = [('Marcus Webb','East', 4250.00),
              ('Priya Sharma', 'West', 5875.50),
              ('Deshawn Carter', 'East',3100.75),
              ('LaTony Rivers', 'South', 3420.00),
              ('Bob Nguyen ','West', 4980.25)]

money_total = 0

for name,region,sales in sales_data:

    money_total += sales 

    if sales >= 5000:

        print(f'{name}({region}): ${sales:,.2f}  <--- top performer')


   
    else:
        print(f'{name} ({region}): $ {sales:,.2f}')
    print(f'Running total {money_total:.2f}\n')
 
print(f'\noverall total sales: ${money_total}:,.2f')
