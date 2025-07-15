# -----------------------------

# 🐍 Python while Loop, break, and continue - Revision Notes

# -----------------------------

# 🔹 Python while Loop

# Used to repeat a block of code while a condition is True.

number = 1
while number <= 3:
print(number)
number += 1

# ✅ Syntax:

# while condition:

# # body of loop

# 👉 The loop continues executing as long as the condition is True.

# If the condition becomes False, the loop stops.

# ⚠️ Remember to update the variable inside the loop to avoid infinite loops.

# 🔹 Example: Input until 0 is entered

number = int(input('Please enter a number: '))

while number != 0:
print(f'Entered number is {number}')
number = int(input('Please enter a number: '))

print('The end')

# 🔹 Infinite while Loop

# num = 25

# while num > 18:

# print('You can vote')

# 🔹 while loop with break

# Use `break` to exit the loop immediately

while True:
name = input('Enter your name: ')
if name == 'end':
print('Loop is ended')
break
print(f'Your name is {name}')

# 🔹 while loop with else

# else block executes when loop ends normally (not with break)

num = int(input('Enter a number: '))

while num > 2:
print(f'Entered number is {num}')
num += 1
else:
print('Inside else block')

# 🔹 for loop vs while loop

# ✅ Use for loop when iterations are known (like over a range or list)

for i in range(4):
print(i)

# ✅ Use while loop when iterations are unknown

while True:
user\_input = input("Enter password: ")
if user\_input == 'exit':
print('Status: Entry Rejected')
break
print('Status: Entry Allowed')

# -----------------------------

# 🔹 Python break and continue

# -----------------------------

# break example:

user\_input = input("Enter password: ")
while True:
if user\_input != 'admin':
print('Not allowed')
break
print('Allowed')

# continue example:

num = 1
while num <= 4:
if num == 2:
num += 1
continue
print(num)
num += 1

# -----------------------------

# ✅ Summary:

# - `while` is used for unknown iteration counts.

# - Use `break` to stop a loop early.

# - Use `continue` to skip current iteration.

# - Always be careful to update loop variables!
