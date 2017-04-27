def gcd(li):
    gcd = 1
    for i in range(1,min(li)+1):
        flag = 0
        for ele in li:
            if ele % i == 0:
                flag += 1
        if flag == len(li):
            gcd = i
    return gcd

def calc():
    result = []
    for i in range(10,100):
        for j in range(i,100):
            i1 = int(str(i)[0:1])
            i2 = int(str(i)[1:2])
            j1 = int(str(j)[0:1])
            j2 = int(str(j)[1:2])
            if i1 == j2:
                if i2/j1 == i/j != 1:
                    result.append([i,j])
            if i2 == j1:
                if j2 != 0:
                    if i1/j2 == i/j != 1:
                        result.append([i,j])
    s,t = 1,1
    for ele in list(map(lambda x: x[0], result)):
        s *= ele
    for ele in list(map(lambda x: x[1], result)):
        t *= ele
    return t//gcd([s,t])

print(calc())
