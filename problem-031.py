def calc():
    coins = [200,100,50,20,10,5,2,1]
    result = 0
    for i0 in range(200//coins[0]+1):
        for i1 in range((200-coins[0]*i0)//coins[1]+1):
            for i2 in range((200-coins[0]*i0-coins[1]*i1)//coins[2]+1):
                for i3 in range((200-coins[0]*i0-coins[1]*i1-coins[2]*i2)//coins[3]+1):
                    for i4 in range((200-coins[0]*i0-coins[1]*i1-coins[2]*i2-coins[3]*i3)//coins[4]+1):
                        for i5 in range((200-coins[0]*i0-coins[1]*i1-coins[2]*i2-coins[3]*i3-coins[4]*i4)//coins[5]+1):
                            for i6 in range((200-coins[0]*i0-coins[1]*i1-coins[2]*i2-coins[3]*i3-coins[4]*i4-coins[5]*i5)//coins[6]+1):
                                result += 1
    return result

print(calc())
