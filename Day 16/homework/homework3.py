# Create a function that calculates the sum of odd and even numbers separately, return a list where these sums are inserted, input data [1,2,3,4,5] ---- output data [6, 9]
def nums(numbers):
    num = 0
    num1 = 0
    for i in range(len(numbers)):
        if i % 2 == 0:
            num = num + numbers[i]
        elif i % 2 != 0:
            num1 = num1 + numbers[i]
    return num,num1
    



my_list = [1,2,3,4,5]
print(nums(my_list))