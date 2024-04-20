my_list = []
my_list1 = []
for i in range(5):
    word = input("please enter word: ")
    my_list.append(word)
operation = input("please enter operation: ")
for i in my_list:
    if my_list.index(i) % 2 == 0:
        my_list1.append(i)
print(operation.join(my_list1))
       


