# Create a function that passes a string. Your task is to remove all spaces from this string and print it
def info(word):
    words = word.split()
    y = "".join(words)
    print(y)


word = "     Goal-   Oriented   Academy    "
info(word)
    

