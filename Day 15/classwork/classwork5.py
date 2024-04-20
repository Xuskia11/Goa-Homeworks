# Create a function that prints the minimum and maximum numbers from a given list
def min_numbers(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    
    for i in numbers:
        if i < min_num:
            min_num = i
        elif i >  max_num:
            max_num = i
    
    print("Minimun number is: ",min_num)
    print("Maxsimum number is: ",max_num)


my_list = [3, 10, 4, 30, 6]
min_numbers(my_list)

