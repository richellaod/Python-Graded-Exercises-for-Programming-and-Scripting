# Richella O'Driscoll 03.24.2018
# Find the Factorial of 5, 7 and 10

def factorial (i):
    number = 1
    while i >= 1:
        number = number * i
        i = i - 1
    return number
    
print (" the factorial of number 5 is:" , factorial (5))
print (" the factorial of number 7 is:" , factorial (7))
print (" the factorial of number 10 is:" , factorial (10))
