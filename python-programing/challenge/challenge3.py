# Challenge:
# Write a function to get the Fibonacci sequence less than a given number.

# The Fibonacci sequence starts with 0 and 1. Each subsequent number is the sum of the previous two.
# For input 22, the return value should be [0, 1, 1, 2, 3, 5, 8, 13, 21]


# input_number = int(input('enter a number : '))
input_number =5
a = 0   
b =1

while  a < input_number:
        # print(a,end=' ')
        print(a)
        # here assigning of a and b shoukd be done parallely otherwise we will get problem
        a, b = b, a+b


# Challenge using for loop:
# Write a function to calculate the factorial of a number.

# The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.
# For example, if n is 5, the return value should be 120 because 1*2*3*4*5 is 120.  

# num = int(input('enter a number : '))
num =5
factorial =1
if num == 0:
 print(f'The factorial of {num} is {factorial}')
i =1
# while i <= num : 
#         factorial*= i 
#         i+=1
# print(factorial)     


while num>1:
     factorial*=num
     num-=1
print(factorial)  

# Program to print odd numbers from 1 to 10

number = int(input('enter a number: '))  
i =1      
while i <= number :
     if i%2 == 0:
        i += 1
        continue
     
     print(f'odd number : {i}')
     i += 1
     
          





