# Create a function to pass to the list. Your task is to print the arithmetic mean (sum / length) of this list.
def nums(numbers):
    all_sum = sum(numbers)
    Arithmetic = all_sum / len(numbers)
    print("arithmetic mean: ",Arithmetic)
    


my_list = [1, 2, 3, 5]
nums(my_list)
