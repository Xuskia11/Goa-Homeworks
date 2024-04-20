#create 3 variable where user input (name,password,repeat_password)
name = input("enter your name: ")
password = input("enter your password: ")
repeat_password = input("repeat your password: ") 

#print and see if user pass is correct or not
if password == repeat_password:
    print("password correct")
else:
    print("password wrong")


