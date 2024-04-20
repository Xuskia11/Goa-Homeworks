user_num = int(input("please entet random number here: "))

if user_num % 2 == 0 and user_num % 3 != 0:
    print("it can be devided into 2")
elif user_num % 3 == 0 and user_num % 2 != 0:
    print("it can be devided into 3")
elif user_num % 2 == 0 and user_num % 3 == 0:
    print("it can be devided into both of them")