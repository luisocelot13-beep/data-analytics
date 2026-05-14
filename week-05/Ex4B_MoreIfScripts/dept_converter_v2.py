Departments ={1: 'Marketing',
              5:'Human Resources',
              10:'Accounting', 
              12:'Legal', 
              18: 'IT',
              20:'Customer Relations'}

department_search = int(input('Type in dept code:'))

match department_search: 

    case 1:
        print(f'Your department is {Departments[1]}')

    case 5:
        print(f'Your department is {Departments[5]}')
    
    case 10:
        print(f'Your department is {Departments[10]}')
    
    case 12:
        print(f'Your departmen is {Departments[12]}')

    case 18:
        print(f'Your department is {Departments[18]}')

    case 20:
        print(f'Your department is {Departments[20]}')

    case _:
        print('Cant find your department')