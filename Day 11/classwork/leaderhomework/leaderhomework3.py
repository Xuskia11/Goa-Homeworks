#Write a program that prompts the user for a password. Continue reading until the correct password is entered. Assume the correct password is "12345678".
password = "12345678"


while True:
    user_pass = input("please enter password: ")
    if user_pass == password:
        break
print("correct")
        