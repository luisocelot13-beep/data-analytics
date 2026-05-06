# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer.

L = ' 101.1'
u  = '55'
i  = '402 stevens'
s  = 'Number 5'

#print(int(float(L)))
# Ranned like normal no errors
# it ranned with int  and having float  it gave me  101

#print(int(float(u)))
# added a .0
# ranned with no issues just a int when print


#print(int(i))
# float error could not convert string to float '402 stevens'
# int error invalid literal for int() with base 10: '402 stevens'
# even after adding int error says could not convert string to float '402 stevens'

#print(int(s))
# float error could not convert string to float 'number 5'
# int error invalid literal for int() with base 10: 'number 5'

L_num = float(L)
u_num = int(u)
i_num = int(i[:3])
s_num = int(s[-1])

print(L_num)
print(u_num)
print(i_num)
print(s_num)