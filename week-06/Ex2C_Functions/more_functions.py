def display_mailing_label(name,address,city,state,zip):
    return(
        f'Hey {name}\n'
        f'{address},{city},{state},{zip}')

print(display_mailing_label('Luis lopez','13016 kelston','winston','NC','27107'))

def add_numbers(*args):
    results = sum(args)

    expression = ' + ' .join(map(str,args))

    return f'{expression} = {results}'

print((add_numbers(1)))

def display_receipt(total_due,amount_paid):
    change_due = amount_paid - total_due
    return( 
        f'Your total due: $ {total_due}\n'
        f'Your amount paid: $ {amount_paid}\n'
        f'Your change:$ {change_due}')

print(display_receipt(20,15))