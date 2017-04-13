def calc():
    index = 2
    num1 = 1
    num2 = 1
    while len(str(num2)) < 1000:
        num = num1 + num2
        num1 = num2
        num2 = num
        index += 1
    return index

print(calc())
