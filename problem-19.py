def count():
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    lean_days = [31,29,31,30,31,30,31,31,30,31,30,31]
    year = 1901
    result = 0
    past = 0
    for ele in lean_days:
        past += ele
    if past % 7 == 0:
        result += 1
    while True:
        if year == 2000:
            lean_days.pop()
            for ele in lean_days:
                past += ele
                if past % 7 == 0:
                    result += 1
            break
        elif year % 4 == 0:
            for ele in lean_days:
                past += ele
                if past % 7 == 0:
                    result += 1
        else:
            for ele in days:
                past += ele
                if past % 7 == 0:
                    result += 1
        year += 1
    return result

print(count())
