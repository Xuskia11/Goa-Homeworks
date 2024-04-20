# Create a function that passes you first and last name. Use split, indexing and print your initials.
def info(fullname):
    names = fullname.split(" ")
    initial1 = names[0][0]
    initial2 = names[1][0]

    initials = initial1 + "." + initial2
    return initials


full_name = input("enter you first and lastname here: ")
print("initials: ",info(full_name))
info(full_name)
