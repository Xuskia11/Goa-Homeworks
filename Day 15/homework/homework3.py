# Create a function that will pass a word and check if it is a palindrome
def palidrome(words):
    if words == words[::-1]:
        print("palidrome")
    else:
        print("not palidrome")


words = input("enter random word here: ")
palidrome(words)
  