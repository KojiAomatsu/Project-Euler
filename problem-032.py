def calc():
    result = []
    for i in range(100):
        for j in range(i,10000):
            k = i*j
            li = [ele for ele in str(i)]
            li += [ele for ele in str(j)]
            li += [ele for ele in str(k)]
            if len(li) == 9:
                li = list(set(li))
                if "0" in li:
                    li.remove("0")
                if len(li) == 9:
                    result.append(k)
    return sum(list(set(result)))

print(calc())
