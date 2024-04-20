def minvalues(numbers):
    num = 1
    for i in numbers:
        if i < num:
            num = i
    return num
print(minvalues([2,4,1,6,7]))