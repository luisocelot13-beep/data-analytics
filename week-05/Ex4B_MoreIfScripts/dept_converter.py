Departments ={1: 'Marketing',
              5:'Human Resources',
              10:'Accounting', 
              12:'Legal', 
              18: 'IT',
              20:'Customer Relations'}

deapartment_search = int(input('Type in dept code:'))

if deapartment_search == 1:
    print(f'Your department is {Departments[1]}')
elif deapartment_search == 5:
    print(f'Your department is {Departments[5]}')
elif deapartment_search == 10:
    print(f'Your department is {Departments[10]}')
elif deapartment_search == 12:
    print(f'Your department is {Departments[12]}')
elif deapartment_search == 18:
    print(f'Your department is {Departments[18]}')
elif deapartment_search == 20:
    print(f'Your department is {Departments[20]}')
else:
    print("Cant find your department")