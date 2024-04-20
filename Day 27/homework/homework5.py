def high_and_low(numbers):
    number = numbers.split(" ")
    x = sorted(number,key=int)
    
    return x[-1] + " " + x[0]