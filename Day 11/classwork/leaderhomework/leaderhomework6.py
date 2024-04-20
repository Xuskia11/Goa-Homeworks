user_degrees = int(input("enter your country temperature now: "))

if user_degrees > 30:
    print("your country is in fire")
elif user_degrees > 20 and user_degrees <= 30:
    print("your country is warm")
elif user_degrees < 20 and user_degrees >= 0:
    print("in your country is cold")
else:
    print("your country is in Antarctica")