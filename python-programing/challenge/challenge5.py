# 1. Reverse a String
# Write a program that takes a string as input and prints its reverse.


course = "mani"


# Solution 1: Using Python Slicing
print(course[::-1])

# Solution 2: Using a loop (for better understanding)
original = "mani"
reversed_str = ""
for char in original:
    print(char)
    reversed_str = char + reversed_str
#     First loop: char is 'h', so reversed_str becomes 'h'.

# Second loop: char is 'e', so reversed_str becomes 'e' + 'h' → 'eh'.

# Third loop: char is 'l', so reversed_str becomes 'l' + 'eh' → 'leh'.
print("Reversed string:", reversed_str)




# 2. Palindrome Checker
# Ask the user for a word and output whether it is a palindrome (reads the same forwards and backwards).

# A palindrome is a sequence—such as a word, phrase, number, or even an entire sentence—that reads the same forward
# and backward when you ignore spaces, punctuation, and capitalization.

pallendrome = input("enter a number or a string : ")
inputValue = pallendrome.lower()
reversed = inputValue[::-1]
if inputValue == reversed:
    print(f'entered value : {inputValue} is a pallendrome ')
else:
    print(f'entered value : {inputValue} is not a pallendrome ')    


# Method 2: Two-Pointer Technique (No Reverse Needed!)
# You can check if the first and last letters match, then move inward with a loop.
#  This way, you don’t even need to build a reversed string!

palindrome = input("Enter a number or a string: ")
input_value = palindrome.lower()
is_palindrome = True

length = len(input_value)
for i in range(length // 2):
    if input_value[i] != input_value[length - 1 - i]:
        is_palindrome = False
        break


# For each i:

# input_value[i]: character from the front.

# input_value[length - 1 - i]: character from the back.

if is_palindrome:
    print(f'Entered value "{palindrome}" is a palindrome.')
else:
    print(f'Entered value "{palindrome}" is not a palindrome.')



# 3. Count Vowels in a String
# Given a sentence, count and print the number of vowels.

# 4. Capitalize Each Word
# Take a sentence and print it with every word’s first letter capitalized.

# 5. Remove Duplicates
# Given a string, return a new string with duplicate characters removed, keeping the first occurrence.