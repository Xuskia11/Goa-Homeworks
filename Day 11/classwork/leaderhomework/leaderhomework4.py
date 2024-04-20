# Create a program that asks the user to continuously enter positive numbers until they enter a negative number. Then print the sum of all positive numbers entered.
while True:
    user_num = int(input("please enter positive nums: "))
    if user_num < 0:
        break
print("you fail")



