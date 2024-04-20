# Create a function to pass to the list. You should have both positive and negative numbers in this list. Your task is to find the number of negative numbers and the sum of positive numbers

def nums(numbers):
    num = 0
    listn = []
    for i in numbers:
        if i >= 0:
            num = num + i
        else:
            listn.append(i)
    print("length of negetive numbers: ", len(listn))

    print("positive numbers sum is: ",num)


my_list = [1, 2, 3, -4, -1]
nums(my_list)