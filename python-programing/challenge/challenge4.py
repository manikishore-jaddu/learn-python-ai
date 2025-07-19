# 1. Python Basics


# Simple Calculator

# Create a command-line calculator that adds, subtracts, multiplies, or divides two numbers.
a = int(input('enter a value : '))
b = int(input('enter b value : '))


print(f'addition for a & b is : {a + b}')
print(f'subtraction for a & b is : {a - b}')
print(f'multiplication for a & b is : {a * b}')


if b!=0: 
 print(f'division for a & b is : {a / b}')
 print(f'floor division for a & b is : {a // b}')
 print(f'modulus for a & b is : {a % b}')
else:
 print('Divison,floor division,modulus with 0 is not possible') 
print(f'Exponentiation  for a & b is : {a ** b}')


# The exponent 0.5 is mathematically the same as a square root:
# number = 16
# square_root = number ** 0.5
# print(f"The square root of {number} is {square_root}")



#2 . New challenge 

# Let the user choose which operation to perform.

# Add support for more operators (like exponentiation, square roots).

# Keep running until the user decides to quit (loop).

# Handle invalid inputs using try/except.


# operator = input('enter operator')
# a = int(input('enter a value : '))
# b = int(input('enter b value : '))


# match operator:
#  case '+'|'add':
#   print(f'addition for a & b is : {a + b}')
#  case '-'|'sub': 
#   print(f'sub for a & b is : {a - b}')
#  case '*'|'multiplication': 
#   print(f'multiplication for a & b is : {a * b}')
#  case '/'|'division': 
#   if b!=0:
#    print(f'division for a & b is : {a / b}') 
#  case '//'|'floor division': 
#   if b!=0:
#    print(f'floor division for a & b is : {a // b}') 
#  case '%'|'modulus': 
#   if b!=0:
#    print(f'mod for a & b is : {a % b}') 
#  case 'exponential': 
#    print(f'expo for a & b is : {a ** b}') 
#  case 'square root': 
#    print(f'square root for a  is : {a ** 0.5}') 
#    print(f'square root for b  is : {a ** 0.5}') 


while True:
    operator = input("Enter operator (+, -, *, /, %, exponent, sqrt, quit): ").strip().lower()
    if operator == "quit":
        print("Exiting calculator. Goodbye!")
        break

    if operator == "sqrt":
        num = float(input("Enter a number for square root: "))
        if num < 0:
            print("Cannot compute square root of a negative number.")
        else:
            print("Square root of", num, "is", num ** 0.5)
        continue

    a = float(input("Enter a value: "))
    b = float(input("Enter b value: "))

    if operator == "+":
        print("Addition:", a + b)
    elif operator == "-":
        print("Subtraction:", a - b)
    elif operator == "*":
        print("Multiplication:", a * b)
    elif operator == "/":
        if b != 0:
            print("Division:", a / b)
        else:
            print("Error: Division by zero!")
    elif operator == "%":
        if b != 0:
            print("Modulus:", a % b)
        else:
            print("Error: Modulus by zero!")
    elif operator == "exponent":
        print("Exponentiation:", a ** b)
    else:
        print("Unknown operator")

   
