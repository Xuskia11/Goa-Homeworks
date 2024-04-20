counter = 0
while True:
    word = input("Please enter a word: ")
    counter += 1
    for i in word:
        if i.islower():
            print("Please enter the word again without lowercase.")
            break
    else:
        break
print("You entered the word without any lowercase letters after", counter, "attempt.")


