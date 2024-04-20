# Abbreviate a Two Word Name
def abbrev_name(name):
    names = name.split(" ")
    initial1 = names[0][0]
    initial2 = names[1][0]

    initials = initial1.upper() + "." + initial2.upper()
    return initials