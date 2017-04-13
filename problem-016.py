def calc():
    num = str(2**1000)
    result = 0
    for ele in num:
        result += int(ele)
    return result

print(calc())
