def square_digits(num):
    num1 = ""
    for i in str(num):
        i = int(i) ** 2
        num1 = num1 + str(i)
    return int(num1)