# Python Strings


print("Hello")
print('hello')

# Quotes Inside Quotes

print('Hi, I am learning "python"')
print("Hi, I am learning 'python'")

# Assign String to a Variable
course = 'python'


# Multiline Strings

aboutPython = """python help's me to learn ai,
need to learn it with data structores & algorithms"""
print(aboutPython)
about = '''python help's me to learn ai,
need to learn it with DSA'''
print(aboutPython)

stringsAreArrays = """Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string."""

print(stringsAreArrays)

print(stringsAreArrays[1])

loopingThroughAString = """Since strings are arrays, we can loop through the characters in a string, with a for loop."""

for x in "banana":
    print(x)

# String Length

a = "hello python"
print(len(a))


# Check String


txt = "I am learning python" 
print("python" in txt)

# Use it in an if statement:
if "i" in txt:
    print("i is present in text")

if "ami" not in txt:
    print("not present")    



# Slicing

courseName = 'python'

print(courseName[0:5])

# Slice From the Start
print(courseName[:4])

# Slice To the End
print(courseName[2:])

# Negative Indexing
print(courseName[-4:-1])



# Python - Modify Strings

# Upper Case
x = 'python'

print(x.upper())

y = 'python Life'

print(y.lower())

# Remove Whitespace
# The strip() method removes any whitespace from the beginning or the end:
print(y.strip())


# Replace String

print(x.replace("p","k"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

print(y.split())


# String Concatenation
a = 'hello'
b= 'python'

print(a+b)

# To add a space between them, add a " ":
print(a +" "+ b)


# String Format
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Placeholders and Modifiers
price = 59
# Add a placeholder for the price variable:
text = f'i bought for {price}'
print(text)


# Display the price with 2 decimals:
text1 = f'i bought for {price:.2f}'
print(text1)


# Perform a math operation in the placeholder, and return the result:
text2 = f'i bought it for {price * 10} dollors'
print(text2)

# Python - Escape Characters

text3 = "we are learning \"python\""


print(text3)


# String Methods

# capitalize()	Converts the first character to upper case
name = "mani KishoRe"
print(name.capitalize())

# casefold()	Converts string into lower case
print(name.casefold())
# center()	Returns a centered string
print(name.center(15))