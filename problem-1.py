def calc():
    sum = 0
    for i in range(1, 1000):
        if i%3 == 0:
            sum += i
        elif i%5 == 0:
            sum += i
    return sum
print(calc())