# Python if...elif..else Statement


# Python if statement : 
# a =int(input('enter a value : '))
a =9
if a > 6:
   print(f'entered value {a} is greater than 6 ')

# to print a value in between the string we need to use f at the begining

# Python if..else statement :    

if a > 0:
    print(f'enetred value {a} is a positive value')   
else:
    print(f'enetred value {a} is a negative value')    

# Python if..elif..else statement :    
    
if a > 0:
    print(f'entered value {a} is positive')
elif a==0:
    print('entered value is zero')  
else:
    print(f'entered value is negative value')      

# Python nested if statement :    


if a > 0:
    print('entered value is positive')

    if a ==0:
        print('entered value is zero')
    else:
        print('entered value is not zero')
else:
    print('entered value is negative')        

# Python for Loop
    
# In Python, we use a for loop to iterate over sequences such as lists, strings, dictionaries, etc. For example,   
languages = ['shift','python','go']

for lang in languages:
  print(lang)

# for loop Syntax  
# for val in sequence:
#     # run this code
# The for loop iterates over the elements of sequence in order, and in each iteration, the body of the loop is executed.

# The loop ends after the body of the loop is executed for the last item.  

for lang in languages:
    print(lang)
    print('-----------------')
# Example: Loop Through a String
courseName = 'python'

for course in courseName:
    print(course)
    print('-----------------')


# for course in courseName:
#     print(course, end= ' ')
#     print('-----------------')

# for course in courseName:
#     print(course,sep='-')    
#     print('-----------------')
    

# for Loop with Python range()     

# Here, range(0, 4) returns a sequence of 0, 1, 2 ,and 3.

# Since the range() function returns a sequence of numbers, we can iterate over it using a for loop. For example, 
for i in range(0,5):
    print(i)  

# Iteration	Value of i	print(i)	Last item in sequence?
# 1st	0	Prints 0 	No
# The body of the loop executes.
# 2nd	1	Prints 1	No
# The body of the loop executes.
# 3rd	2	Prints 2	No
# The body of the loop executes.
# 4th	3	Prints 3	Yes
# The body of the loop executes and the loop terminates.           

# iterate from i = 0 to 3
for _ in range(0, 4):
    print('Hi')
# break and continue Statement
# The break and continue statements are used to alter the flow of loops.

for lang in languages:
    if lang == 'go':
     break
    print(lang)  
# The continue Statement
for lang in languages:
    if lang == 'python':
      continue
    print(lang)    
# Nested for loops
attributes = ['Electric', 'Fast'] 
cars = ['tesla','benz','bmw'] 



for attribute in attributes :
    for car in cars:
        print(attribute, car)