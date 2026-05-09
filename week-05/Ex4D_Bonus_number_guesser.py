import random
 

numbers = list(range(1,11))
# 1 2 3 4 5 6 7 8 9 10 
numbers.reverse() # after reversing them look below 


# list of number is 10 9 8 7 6 5 4 3 2 1

secret_number = numbers[3] # the number is 7


print('Guess a number between 1 and 10 ')

Number_guess  = 0

Time_guessed = 0



guessed_numbers = []


while Number_guess != secret_number:

    Number_guess = int(input('Please guess a number 1 - 10:'))

    Time_guessed += 1
    
    guessed_numbers.append(Number_guess)

   

    if Number_guess < secret_number:
        print('Higher')

    elif Number_guess > secret_number:
        print('Lower')

if  Time_guessed < 5:
    print('Your awesome under 5 guesses')


print('Correct ,you guessed the number')
print(f' the amount of times you guessed {Time_guessed}')

print(f'The numbers you guessed {guessed_numbers}')