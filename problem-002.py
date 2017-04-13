def calc():
    sum = 0
    num1 = 1
    num2 = 1
    while num2 < 4000001:
        if num2 % 2 == 0:
            sum += num2
        num = num1 + num2
        num1 = num2
        num2 = num
    return sum

print(calc())
