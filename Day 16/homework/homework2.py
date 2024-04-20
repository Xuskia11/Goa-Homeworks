# Create a function that will return the sum of the numbers in the list at even indices, input data: [1,2,3,4,5] ---- output data (result): 9
def nums(numbers):
    num = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            num = num + numbers[i]
    return num


my_list = [1,2,3,4,5]
print(nums(my_list))
