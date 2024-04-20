# Create a function that takes a list as an argument and prints the sum of the numbers in the list
def nums(numbers):
    num = 0
    for i in numbers:
        num = num + i
    print("sum all of numbers is: ",num)

nums_list = [2, 3, 4, 6]
nums(nums_list)