num = int(input("please enter random number here: "))
num1 = int(input("please enter random number here: "))
sums = 0
if num % 2 == 0:
    for i in range(num,num1 + 1,2):
        sums = sums + i
else:
    for i in range(num + 1,num1 + 1,2):
        sums = sums + i
print(sums)

        
    