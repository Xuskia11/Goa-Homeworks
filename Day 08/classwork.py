i = 2
while i < 40:
    print(i)
    i = i + 2



result = 0
i = 0
while i <= 5:
    result = result + i
    i = i + 1
    print(result)




for i in range( 0,10,2):
    print(i)



password = "xuskia1102"
guess = input()
while guess != password:
    guess = input()
print("acces granted")




age = int(input("how old are you"))
if age >= 18:
    print("you are an adult")
else:
    print("you aren't an adult")
