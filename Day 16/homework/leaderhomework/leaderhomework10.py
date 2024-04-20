num = int(input("please enter random number here: "))
my_list = []
while True:
    num = int(input("please enter random number here: "))
    if num == 0:
        break
    else:
        my_list.append(num)
print(max(my_list))
