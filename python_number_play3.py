"""
This module prompts the user to enter an integer and then
checks whether the number is negative, zero, or positive.
"""

x = int(input("Please enter an integer: "))

print('You entered: ' + str(x))

# if-else logic
if x < 0:
    print('The number is negative')
elif x == 0:
    print('The number is 0')
else:
    print('The number is > 0')
