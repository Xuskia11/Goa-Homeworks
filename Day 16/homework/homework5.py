# Create a copy of the replace
def cars(word):
    my_list = ["GTR", "BMW", "MERCEDES"]
    my_list[1] = word
    return my_list

print(cars("GOLF"))
