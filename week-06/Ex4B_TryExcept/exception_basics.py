# ValueError = A ValueError occurs if you send a string into a function that requires a number:
# x = float('hello')

# NameError = You get a NameError if you use a variable that does not exist:
# print(x)

# TypeError = A TypeError occurs if you try to concatenate a string and a number:
# x = "hello"
# y = 15
# print(x + y)


# SyntaxError =	Raised when a syntax error occurs
try :
    x = float('hello')
except ValueError:
    print('Valueerror: OOps seems like you put a non number in a float or int that may require it')
else:
    print(x)
finally:
    print('Lets try another one')

try :
    print(z)
except NameError:
    print('NameError: oopsk looks like your printing a value without it being assigned')
else:
    print(z)
finally:
    print('lets try another one ok?')

try :
    x = "hello"
    y = 15
    print(x + y)
except TypeError:
    print('Oh dang sems like your adding two different types of values')
else:
    print('no error occured')

finally:
    print('lets try another one')

try :
    eval('x===5')

except SyntaxError:
    print('SyntaxError:Invalid syntax detected')
else:
    print('No errors occured')
finally:
    print('Lets try another one')