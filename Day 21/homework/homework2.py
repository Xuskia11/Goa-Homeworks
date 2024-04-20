def bmi(weight, height):
    y = weight / (height ** 2)
    if y  <= 18.5:
        return "Underweight"
    elif y <= 25.0:
        return "Normal"
    elif y <= 30.0:
        return "Overweight"
    else:
        return "Obese"
print(bmi(15,20))

