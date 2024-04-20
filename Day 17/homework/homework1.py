def learn(word,char_to_find):
    return  (word.lower()) + " " + (word.upper()) + " " + (word.capitalize()) + " " + str(word.find(char_to_find))
print(learn("gamarjoba", "a"))