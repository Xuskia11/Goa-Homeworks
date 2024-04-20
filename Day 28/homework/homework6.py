def solution(s):
    x = ""
    for i in s:
        if i != i.upper():
            x += i
        elif i == i.upper():
            x += " " + i
    return x