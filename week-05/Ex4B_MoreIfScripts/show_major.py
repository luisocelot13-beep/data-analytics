Major_inf = {'BIOL': ('Biology','Sciend Bldg, Room 310'),
             'CSCI': ('Computer Science','Sheppard Hall, Room 314'),
             'ENG' : ('English','Kerr Hall, Room 201'),
             'HIST': ('History', 'Kerr Hall, Room 114'),
             'MKT' : ('Marketing', 'Westly Hall, Room 310')


}





student_name = input(' Type in full name:')

student_major_code = input('enter major code: eX.)BIOL,CSCI,ENG:').upper()

if student_major_code in Major_inf:

    Major_name,office = Major_inf[student_major_code]

    print(f'Hey {student_name}, your major is {Major_name},your department is {office}')
else:
    print('Invalid code ')