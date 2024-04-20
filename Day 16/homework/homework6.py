#  Create a copy of the join function
def joins(my_list):
    numbers = ""
    for i in my_list:
        numbers = numbers + i + " "
    return numbers

my_lists = ["cars","fruits","vagetable", "comtuter"]
print(joins(my_lists))
