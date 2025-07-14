# Challenge with if else :
# Write a function to check whether a student passed or failed his/her examination.

# Assume the pass marks to be 50.
# Return Passed if the student scored more than 50. Otherwise, return Failed.



studentName = input('enter student name :')
studentMarks = int(input('enter student marks :'))

pass_marks = 50
maxMarks = 100

if studentMarks >= pass_marks :
    print(f'{studentName} passed in the exams by scoring {studentMarks} out of {maxMarks}')
else:
    print(f'{studentName} failed in the exams by scoring {studentMarks} out of {maxMarks}')

# Challenge using for loop:
# Write a function to calculate the factorial of a number.

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# For example, if n is 5, the return value should be 120 because 1*2*3*4*5 is 120.        
    

number = int(input('enter number to calculate factorial : '))
factorial=1
# step 1 : need to get the range like if the number is 4 we need to get 1,2,3,4
# Changed "number <= 0" ➜ "number < 0"
# Because factorial of 0 is valid and equals 1.
if number < 0:
    print('number is invalid for factorial')
else:    
  for i  in range(1,number+1):
    # step2 : calculate 1 *2*3*4 is the factorial of 4 
     factorial *= i
  print(f'The factorial of {number} is {factorial}')

