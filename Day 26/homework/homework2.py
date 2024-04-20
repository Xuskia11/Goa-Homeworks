def maxvalues(numbers):
    num = 0
    for i in numbers:
        if i > num:
            num = i
    return num
print(maxvalues([2,4,1,6,7]))
        
    

