# Write an algorithm that prints whether a number entered by the user is positive, negative, or zero.
num = int(input("please enter random number here: "))

if num == 0:
    print("your number is zero")
elif num > 0:
    print("your number is positive")
else:
    print("your number is negative")