def calc():
    li = []
    for a in range(2,101):
        for b in range(2,101):
            li.append(a**b)
    li_uniq = list(set(li))
    return len(li_uniq)

print(calc())
