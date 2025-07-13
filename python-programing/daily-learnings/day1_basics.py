# printing
print("Hello,world!")

# Python Variables and Literals
# Python Variables

number =10

# Assigning values to Variables in Python
site_name = 'manikishore'

print(site_name)

# Changing the Value of a Variable in Python
site_name ='python'
print(site_name)

# Example: Assigning multiple values to multiple variables
a,b,c = 1,2.2,'python'
print(a)
print(b)
print(c)

# If we want to assign the same value to multiple variables at once, we can do this as: 
site1=site2 = 'pythonLife'

print(site1)
print(site2)



# Rules for Naming Python Variables
# 1. Constant and variable names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_). For example:

# snake_case
# MACRO_CASE
# camelCase
# CapWords
# 2. Create a name that makes sense. For example, vowel makes more sense than v.

# 3. If you want to create a variable name having two words, use underscore to separate them. For example:

# my_name
# current_salary
# 5. Python is case-sensitive. So num and Num are different variables. For example,

# var num = 5 
# var Num = 55
# print(num) # 5
# print(Num) # 55
# 6. Avoid using keywords like if, True, class, etc. as variable names.

# Python Literals
# site_name = 'programiz.com'
# In the above expression, site_name is a variable, and 'programiz.com' is a literal.


# Python Numeric Literals
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 
# different numerical types: Integer, Float, and Complex.

# 1. Integer Literals
# Integer literals are numbers without decimal parts. It also consists 
# of negative numbers. For example, 5, -11, 0, 12, etc.

x = 1
y = -1
print(x)
print(y)
 

# 2. Floating-Point Literals
# Floating-point literals are numbers that contain decimal parts.

# Just like integers, floating-point numbers can also be both positive and negative. For example, 2.5, 6.76, 0.0, -9.45, etc.
c = 1.1
d = - 0.1
print(c)
print(d)

# 3. Complex Literals
# Complex literals are numbers that represent complex numbers.

# Here, numerals are in the form a + bj, where a is real and b is imaginary. For example, 6+9j, 2+3j.

# e = x + y *1j
# print(e)

# Or use the built-in complex() function:

e = complex(x, y)
print(e)

# Python String Literals
# In Python, texts wrapped inside quotation marks are called string literals..

print("This is a string.")
# We can also use single quotes to create strings.

print('This is also a string.')

# Python Boolean Literals
# There are two boolean literals: True and False.
is_pass = True
print(is_pass)


# Character Literals in Python
# Character literals are unicode characters enclosed in a quote. For example,
some_character = 'K'
print(some_character)
# Here, K is a character literal assigned to some_character.



# Special Literal in Python
# Python contains one special literal None. We use it to specify a null variable. For example,

value = None

print(value)
# Here, we get None as an output as the value variable has no value assigned to it.



# Collection Literals
# Let's see examples of four different collection literals. List, Tuple, Dict, and Set literals.

# list literal
fruits = ['mango','grapes','mosambi']
print(fruits)

# tuple literal
numbers = (1,2,3)
print(numbers)

# dictionary literal
alphabets = {'a':'apple',"b":"ball"} 
print(alphabets)

# set literal
vowels = {'a', 'e', 'i' , 'o', 'u'} 
print(vowels)

# In the above example, we created a list of fruits, a tuple of numbers, a dictionary of alphabets having values with keys designated to each value and a set of vowels.



