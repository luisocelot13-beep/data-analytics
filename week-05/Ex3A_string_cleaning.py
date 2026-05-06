import math
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

salary_clean_1 = int(salary_1.replace('$','').replace(',',''))
salary_clean_2 = int(salary_2.replace('$','').replace(',',''))
# just do it once an just include type in print

print(name_1.lower().title())
print(name_2.lower().title())
print(name_3.lower().title())

 # print(type(int(salary_1.replace('$','').replace(',','')))) manually do it in print

print(type(salary_clean_1))