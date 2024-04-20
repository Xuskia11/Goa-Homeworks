name = input("please enter your name here: ")
letter = input("please enter here letter what you want to find: ")
y = []
for i in name:
    y.append(i)
if letter in name:

    print(y.index(letter))

else:
    print(-1)