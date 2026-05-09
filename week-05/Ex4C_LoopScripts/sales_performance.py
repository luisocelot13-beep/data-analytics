sales_data = [('Marcus Webb','East', 4250.00),
              ('Priya Sharma', 'West', 5875.50),
              ('Deshawn Carter', 'East',3100.75),
              ('LaTony Rivers', 'South', 3420.00),
              ('Bob Nguyen ','West', 4980.25)]

money_total = 0

for name,region,sales in sales_data:

  print(f'{name}({region}): ${sales:,.2f}')
  money_total += sales

  print(f'{money_total:,.2f}')

  if sales >= 5000:
    print(f'Top performer')

print(f'\noverall total sales: ${money_total}:,.2f')
