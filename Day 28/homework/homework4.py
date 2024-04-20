def reverse_words(text):
    x = text.split(" ")
    lists = []
    for i in x:
        lists.append(i[::-1])
        
    return " ".join(lists)