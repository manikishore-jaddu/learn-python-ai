# Write to split the restaurant bill among friends.

# Take the subtotal of the bill and the number of friends as inputs.
# Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.
# Return the amount each friend has to pay, rounded off to two decimal places.

# step 1 : Take the subtotal of the bill and the number of friends as inputs.
total = float(input('enter total bill amount :'))
noOfFriends = int(input('enter total number of friends :'))

# step 2 : Calculate the total bill by adding 20% tax to the subtotal and then divide it by the number of friends.

tax = total * 0.20
total += tax
eachFriendNeedsToPay = round(total/noOfFriends,2)
# Return the amount each friend has to pay, rounded off to two decimal places.
print('each friend needs to pay in rupes :',eachFriendNeedsToPay)
