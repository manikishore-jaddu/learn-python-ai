# -----------------------------

# 🐍 Python Basics Revision Notes

# -----------------------------

# 🔹 Python Type Conversion

# There are 2 types of type conversion: Implicit and Explicit

# ✅ Implicit Conversion:

int\_number = 2
float\_number = 3.3
value = int\_number + float\_number
print(value)
print(type(value))

# ✅ Explicit Conversion (Type Casting):

int\_number = 5
string\_number = '5'
valueCheck = int\_number + int(string\_number)
print(valueCheck)
print(type(valueCheck))

# 🔹 Python Basic Input and Output

print('Python is powerful')

# Syntax: print(object, sep=, end=, file=, flush=)

print('learning python', end=' ')
print('because I want to become an AI engineer')
print('my', 'age', 'is', 2, 'years', sep='.')
print('python' + 'life')

a = 10
b = 20
print('The value of a = {} and b = {}'.format(a, b))

num = input('Please enter your age: ')
print('You entered:', num)
print(type(num))

number = int(input('Enter your phone number: '))
print('Entered phone number:', number)
print('Type:', type(number))

# 🔹 Python Operators Overview

# 1. Arithmetic

# 2. Assignment

# 3. Comparison

# 4. Logical

# 5. Bitwise

# 6. Special

# ✅ Arithmetic Operators

a = int(input('Enter a value: '))
b = int(input('Enter b value: '))

print('Addition:', a + b)
print('Subtraction:', a - b)
print('Multiplication:', a \* b)
print('Division:', a / b)
print('Floor Division:', a // b)
print('Modulo:', a % b)
print('Power:', a \*\* b)

# ✅ Assignment Operators

x = int(input('Enter x value: '))
print('Entered value:', x)
x += 1
print('Addition Assignment:', x)
x -= 1
print('Subtraction Assignment:', x)
x \*= 4
print('Multiplication Assignment:', x)
x /= 4
print('Division Assignment:', x)
x //= 5
print('Floor Division Assignment:', x)
x %= 2
print('Remainder Assignment:', x)
x \*\*= 2
print('Exponent Assignment:', x)

# ✅ Comparison Operators

a = 5
b = 10
print('Is Equal To:', a == b)
print('Not Equal To:', a != b)
print('Greater Than:', a > b)
print('Less Than:', a < b)
print('Greater Than or Equal To:', a >= b)
print('Less Than or Equal To:', a <= b)

# ✅ Logical Operators

a = 5
b = 6
print((a > 2) and (b >= 6))
print((a > 2) or (b >= 6))
print(not a > 10)

print(not 0)        # True
print(not 10)       # False
print(not "")       # True
print(not "hello")  # False

# ✅ Bitwise Operators

x = 10  # 1010 in binary
y = 4   # 0100 in binary

print('Bitwise AND:', x & y)      # 0000 = 0
print('Bitwise OR:', x | y)       # 1110 = 14
print('Bitwise XOR:', x ^ y)      # 1110 = 14
print('Bitwise NOT:', \~x)         # -11
print('Left Shift:', x << 1)      # 10100 = 20
print('Right Shift:', x >> 1)     # 0101 = 5

# ✅ Special Operators

# 🔸 Identity Operator: is, is not

x = \[1, 2, 3]
y = \[1, 2, 3]
z = x
print(x is z)         # True
print(x is y)         # False
print(x is not z)     # False
print(x == y)         # True

# 🔸 Membership Operator: in, not in

print('n' in 'membership')         # True
my\_list = \[1, 2, 3]
print(3 in my\_list)                # True
my\_tuple = (1, 2, 3)
print(1 in my\_tuple)               # True
my\_set = {1, 2, 3}
print(1 in my\_set)                 # True
my\_dict = {'a': '1', 'b': '2'}
print('a' in my\_dict)              # True
print('1' in my\_dict.values())     # True
