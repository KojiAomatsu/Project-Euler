def calc():
    result = 1
    for i in range(20):
        result *= i + 21  
    for i in range(20):
        result /= i + 1
    return result

print(calc())
