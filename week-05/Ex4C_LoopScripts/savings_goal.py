start_balance = 100
weekly_saving = 100
treat_amount = 20
saving_goal = 1000

while start_balance < saving_goal:
    start_balance += weekly_saving
    print(f'this week my balance is {start_balance}')

    if start_balance >= saving_goal * 0.75 and start_balance < saving_goal:
        balance_after_treat = start_balance -treat_amount
        print(f'so close, after your treat your balance is {balance_after_treat}')


print(f'met my goal current balance is {start_balance}')