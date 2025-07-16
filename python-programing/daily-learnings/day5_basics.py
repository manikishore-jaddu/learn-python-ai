n = 10

# use pass inside if statement
if n > 10:
    pass

print('Hello')


# 2. match-case
day = "Monday"
match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("Weekend coming")
    case _:
        print("Just another day")
