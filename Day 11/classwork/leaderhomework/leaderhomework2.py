#Write a program that prompts the user for numbers continuously until they enter 0.
summation = 0 

while True:
    num = int(input("please enter random number: "))
    if num == 0:
        break
    else:
        summation = summation + num

print("summation of all your numbers is", summation)
    

