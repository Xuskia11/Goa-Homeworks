def number(bus_stops):
    num = 0
    num1 = 0
    for i in bus_stops:
        num = i[0] - i[1]
        num1 = num1 + num
    return num1