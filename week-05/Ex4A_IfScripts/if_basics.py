x = 100 
y = 20

if x / y == 5:
    print("x divided by 20 is 5")
    x = 1
else:
    print("are the variables set up correctly?")


if x * y == y:
    print('now x * y is 5')
    x = 10
else:
    print('Whoops, x equals'+ str(x))

if x < y:
    print('x is less than y')
    x = x * 2
else:
    print('Uh oh, x is not less than y')

if x > y:
    print('how is x greater than y?')
else:
    print('X is not greater than y')

print(f'The final value of x is {x} and the final value of y is {y}')