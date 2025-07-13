# Python Type Conversion

# there are 2 types of type conversion 
# 1. Implicit 
# 2. Explicit 

# 1. Implicit example : 

int_number =2
float_number = 3.3

value = int_number + float_number
print(value)
print(type(value))


# 2. Explicit example :  which is called Type Casting,
int_number = 5
string_number = '5'
# here we are getting type conversion error  : TypeError: unsupported operand type(s) for +: 'int' and 'str'
# valueCheck = int_number + string_number
# here we need convert the type explicitly

valueCheck = int_number + int(string_number)
print(valueCheck)
print(type(valueCheck))



# Python Basic Input and Output

print('python is powerfull')

# Syntax of print()
# print(object= separator= end= file= flush=)

print('lets check this print examples ')
print('python')
# here in above example i can see the there is no end part but by default it chose to \n so let change this first
print('learning python' ,end= ' ')
print('because i want to become ai engineer')


# lets use this seperator now
print('my age is',2,'years',sep='.')


# Print Concatenated Strings
print('python'+'life')

# Output formatting
a=10
b=20
print('the value of a = {} and b  = {} '.format(a,b) )

# Python Input
num = input('please enter you age: ')
print('you entered :',num)
print(type(num))
# everytime i can see like string will be returning here so explicitly we need to convert
number = int(input('enter your phone number :'))
print('entered phone number :',number)
print('type :',type(number))


# Python Operators
# we do have 6 operators : 
# 1. Arithematic
# 2. Assignment
# 3. comparission
# 4. logical
# 5. bitwise
# 6.special


# 1. Arithmetic Operator :
a = int(input('enter a value :'))
b = int(input('enter b value :'))



print('Addition',a+b)
print('Substraction',a-b)
print('multiplication',a*b)
print ('division',a/b)

# ✅ 1. // → Floor Division
# It divides two numbers and rounds down the result to the nearest whole number (also called "integer division").

# Even if the result is a float, it gets floored (i.e., rounded towards negative infinity).
# print(10 // 3)   # ➜ 3 (because 10 ÷ 3 = 3.333..., floor is 3)
# print(10 // 2)   # ➜ 5
# print(-10 // 3)  # ➜ -4 (floor of -3.33 is -4)

print ('floor division ',a//b)

#  2. % → Modulo (Remainder)
# It gives you the remainder after division.

# Often used to check even/odd, wrap-around, or cycles.
print ('modulo',a%b)
# 3. ** → Exponentiation (Power)
# Raises the first number to the power of the second number.
# print(4 ** 2)   # ➜ 16 (4 squared)
# print(2 ** 3)   # ➜ 8 (2 cubed)
# print(5 ** 0)   # ➜ 1 (any number to power 0 is 1)

print('power',a**b)



# 2. Python Assignment Operators


# Operator	Name	Example
# =	Assignment Operator	a = 7
# +=	Addition Assignment	a += 1 # a = a + 1
# -=	Subtraction Assignment	a -= 3 # a = a - 3
# *=	Multiplication Assignment	a *= 4 # a = a * 4
# /=	Division Assignment	a /= 3 # a = a / 3
# %=	Remainder Assignment	a %= 10 # a = a % 10
# **=	Exponent Assignment	a **= 10 # a = a ** 10

x = int(input('enter x value :'))
print('enterd value : ',x)
x+=1
print('Addition Assignment : ',x)
x-=1
print('Subtraction Assignment : ',x)
x*=4
print('Multiplication Assignment : ',x)
x/=4
print('Division Assignment : ',x)
x//=5
print('Floor Division Assignment : ',x)

x%=2
print('Remainder Assignment : ',x)
x**=2
print('Exponent Assignment : ',x)


# 3. Python Comparison Operators

# Operator	Meaning	Example
# ==	Is Equal To	3 == 5 gives us False
# !=	Not Equal To	3 != 5 gives us True
# >	Greater Than	3 > 5 gives us False
# <	Less Than	3 < 5 gives us True
# >=	Greater Than or Equal To	3 >= 5 give us False
# <=	Less Than or Equal To	3 <= 5 gives us True


a =5
b=10


print('Is Equal To : ' , a==b)
print('Not Equal To : ' , a!=b)
print('Greater Than : ' , a>b)
print('less Than : ' , a<b)
print('Greater Than or Equal To : ' , a>=b)
print('less Than or Equal To : ' , a<=b)


# 4. Python Logical Operators
# Operator	Example	Meaning
# and	a and b	Logical AND:
# True only if both the operands are True
# or	a or b	Logical OR:
# True if at least one of the operands is True
# not	not a	Logical NOT:
# True if the operand is False and vice-versa.


a = 5
b = 6

print((a > 2) and (b >= 6)) 
print((a > 2) or (b >= 6)) 
print(not a > 10) 


print(not 0)        # True (because 0 is False)
print(not 10)       # False (10 is True)
print(not "")       # True (empty string is False)
print(not "hello")  # False (non-empty string is True)



# 5. Python Bitwise operators
# Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

# For example, 2 is 10 in binary, and 7 is 111.

# In the table below: Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)

# Operator	Meaning	Example
# &	Bitwise AND	x & y = 0 (0000 0000)
# |	Bitwise OR	x | y = 14 (0000 1110)
# ~	Bitwise NOT	~x = -11 (1111 0101)
# ^	Bitwise XOR	x ^ y = 14 (0000 1110)
# >>	Bitwise right shift	x >> 2 = 2 (0000 0010)
# <<	Bitwise left shift	x 0010 1000)


# Python has two special operators:

# is → Identity operator

# in → Membership operator


# 🔸 1. is → Identity Operator
x= [1,2,3]
y= [1,2,3]
z=x

print(x is z)
print(x is y)
print(x is not z)
print(x == y)
# Use == to compare values, is to compare identity (memory address).


# 🔸 2. in → Membership Operator
# Used to check if a value exists in a sequence (string, list, tuple, set, dictionary).


print ('string'in'in memborship operator string check ')
my_list = [1,2,3]
print (3 in my_list)

my_tuple = (1,2,3)
print (1 in my_tuple)

my_set = {1,2,3}
print (1 in my_set)

my_dict = {'a':"1","b":"2"}
print ('a' in my_dict)
print ('1' in my_dict.values())