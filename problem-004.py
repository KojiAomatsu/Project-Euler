def calc():
    numbers = []
    palindromic = []
    for i in range(900, 1000):
        for j in range(900, 1000):
            numbers.append(i*j)
    for num in numbers:
        if str(num) == str(num)[::-1]:
            palindromic.append(num)
    palindromic.sort()
    return palindromic[-1]

print(calc())
