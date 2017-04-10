def calc():
    lis = []
    for i1 in range(3):
        remem = ['0','1','2','3','4','5','6','7','8','9']
        j1 = remem.pop(i1)
        for i2 in range(9):
            j2 = remem.pop(i2)
            for i3 in range(8):
                j3 = remem.pop(i3)
                for i4 in range(7):
                    j4 = remem.pop(i4)
                    for i5 in range(6):
                        j5 = remem.pop(i5)
                        for i6 in range(5):
                            j6 = remem.pop(i6)
                            for i7 in range(4):
                                j7 = remem.pop(i7)
                                for i8 in range(3):
                                    j8 = remem.pop(i8)
                                    for i9 in range(2):
                                        j9 = remem.pop(i9)
                                        j10 = remem.pop()
                                        lis.append(j1+j2+j3+j4+j5+j6+j7+j8+j9+j10)
                                        remem.append(j10)
                                        remem.append(j9)
                                        remem.sort()
                                    remem.append(j8)
                                    remem.sort()
                                remem.append(j7)
                                remem.sort()
                            remem.append(j6)
                            remem.sort()
                        remem.append(j5)
                        remem.sort()
                    remem.append(j4)
                    remem.sort()
                remem.append(j3)
                remem.sort()
            remem.append(j2)
            remem.sort()
    return lis[999999]

print(calc())
