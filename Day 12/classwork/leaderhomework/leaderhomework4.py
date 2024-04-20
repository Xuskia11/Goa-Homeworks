# Ask the user for any number from 1 to 9 inclusive. Then use a for loop and output multiples of that number in the range 1 to 50.
user_num = int(input("please enter number 1 to 9: "))

if user_num < 1 or user_num > 9:
    print("you wrote a incorrect number: ")

for i in range(1, 50):
    if i % user_num == 0:
        print(i)




    