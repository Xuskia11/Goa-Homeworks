def join(listn):
    sentence = ""
    for i in listn:
        sentence = sentence + i
    return sentence
print(join(["goal", "Oriented", "academy"]))