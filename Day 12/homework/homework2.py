#Enter a negative number for the user. Add all negative numbers from this number to 0 to the list and finally print the list
number = int(input("enter here negative number: "))
list = []
while number < 0:
    list.append(number)
    number = number + 1
print(list)
    

