word = input("please enter random word here: ")
my_list = []
my_lists = []
for i in word:
    my_list.append(i)
    if my_list.index(i) % 2 == 0:
        my_lists.append(i.upper())
    else:
        my_lists.append(i.lower())

if len(my_lists) % 2 == 0:
    my_lists[-1] = my_lists[-1].lower()
else:
    pass

print("".join(my_lists))