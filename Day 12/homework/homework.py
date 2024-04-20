#Enter the user's first name, last name, age and place of residence
name = input("enter your name here: ")
lastname = input("enter your lastname here: ")
age = int(input("enter you age here: "))
place = input("enter you dwelling place: ")
list = []
#Enter the user's first name, last name, age and place of residence
list.append(name)
list.append(lastname)
list.append(age)
list.append(place)
print(list)
#Using slicing, print 1: First Name, Last Name, 2: Last Name, Age, 3: First Name, Last Name, Age 4: Last Name, Age, Residence.
print(list[0:2])
print(list[1:3])
print(list[0:3])
print(list[1:4])