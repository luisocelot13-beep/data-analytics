a = 13
b = 8 
c = 26


# find the smalles

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# find the biggest number

if a >= b and a >= c:
    largest = a

elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f'smallest number {smallest}')
print(f'largest number is: {largest}')