def calc():
    num = 1
    for i in range(100):
        num *= i+1
    result = 0
    for ele in str(num):
        result += int(ele)
    return result

print(calc())
