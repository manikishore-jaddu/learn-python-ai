# -----------------------------

# 🐍 Python Control Flow and Loops Notes

# -----------------------------

# 🔹 Python if...elif...else Statement

# ✅ if statement:

a = 9
if a > 6:
print(f'entered value {a} is greater than 6')

# ✅ if...else statement:

if a > 0:
print(f'entered value {a} is a positive value')
else:
print(f'entered value {a} is a negative value')

# ✅ if...elif...else statement:

if a > 0:
print(f'entered value {a} is positive')
elif a == 0:
print('entered value is zero')
else:
print(f'entered value is negative')

# ✅ Nested if statement:

if a > 0:
print('entered value is positive')

```
if a == 0:
    print('entered value is zero')
else:
    print('entered value is not zero')
```

else:
print('entered value is negative')

# 🔹 Python for Loop

# Used to iterate over sequences (list, string, etc.)

languages = \['shift', 'python', 'go']

for lang in languages:
print(lang)

# Loop with extra print line:

for lang in languages:
print(lang)
print('-----------------')

# Loop through a string:

courseName = 'python'
for course in courseName:
print(course)
print('-----------------')

# Loop using range():

# range(0, 5) → 0 to 4

for i in range(0, 5):
print(i)

# Loop from 0 to 3 without using variable:

for \_ in range(0, 4):
print('Hi')

# 🔹 break and continue statements

# break → stops the loop when condition is met

for lang in languages:
if lang == 'go':
break
print(lang)

# continue → skips the current iteration

for lang in languages:
if lang == 'python':
continue
print(lang)

# 🔹 Nested for loops

attributes = \['Electric', 'Fast']
cars = \['tesla', 'benz', 'bmw']

for attribute in attributes:
for car in cars:
print(attribute, car)
