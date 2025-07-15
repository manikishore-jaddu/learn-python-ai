# Python while Loop
# In Python, we use a while loop to repeat a
#  block of code until a certain condition is met. For example,


number = 1
while number <=3:
    print(number)
    number+=1

#  In the above example while loop will run untill the above condition is true

# while loop syntax   
# while condition:
    # body of the loop

#  Here,

# The while loop evaluates condition, which is a boolean expression.
# If the condition is True, body of while loop is executed. The condition is evaluated again.
# This process continues until the condition is False.
# Once the condition evaluates to False, the loop terminates.   


# Tip: We should update the variables used in condition inside the loop so that it eventually evaluates to False. Otherwise, the loop keeps running, creating an infinite loop.

# Flowchart of Python while Loop

# Example: Python while Loop

number = int(input('please enter a number : '))

while number!=0:
    print(f'entered number is {number}')
    number = int(input('please enter a number : '))

print('the end')


# Infinite while Loop
# num = 25
# while num > 18 :
#     print('you can vote')

# Python while loop with break statement

# We can use a break statement inside a while loop 
# to terminate the loop immediately without checking the test condition. For example,
while True:
    name = input('enter your name : ')
    if name == 'end':
     print('loop is ended')
     break

    print(f'your name is {name}')
#  Here, the condition of the while loop is always True. However, 
# if the user enters end, the loop termiantes because of the break statement.   



# Python while loop with else statement

num = int(input('enter a number : '))

while num >2:
   print(f'enetered number is {num}')
   num+=1
else:
   print('inside else block')


# Python for loop vs while loop

# The for loop is usually used in the sequence when the number of iterations is known. For example,
# loop is iterated 4 times 
for i in range(4):
    print(i)

# The while loop is usually used when the number of iterations is unknown. For example,
while True:
    user_input = input("Enter password: ")

    # terminate the loop when user enters exit
    if user_input == 'exit':
        print(f'Status: Entry Rejected')
        break  

    print(f'Status: Entry Allowed')



# Python break and continue

user_input = input("Enter password: ")
while True:
   if user_input !='admin':
      print('not allowed')
      break
   print('allowed')   


num =1

while num <= 4:
   if num == 2:
      continue
   print(num)
   num+=1