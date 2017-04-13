def calc():
    high_score = 1
    result = 1
    for i in range(2, 1000):
        rests = []
        rest = 1
        for _ in range(i):
            m = rest * 10
            rest = m % i
            if rest in rests:
                score = len(rests) - rests.index(rest)
                if score > high_score:
                    high_score = score
                    result = i
                break
            else:
                rests.append(rest)
        rests.clear()
        rest = 1
    return result

print(calc())
