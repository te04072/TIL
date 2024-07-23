
T = int(input())

def moneyCount(money, coin):
    moneySet = [money // coin, money % coin]
    return moneySet

for test_case in range(1, T + 1):
    price = int(input())
    moneyKey = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    output = [0]*len(moneyKey)
    leftover = 0
    for i in range(len(moneyKey)):
        [output[i], leftover] = moneyCount(price, moneyKey[i])
        price = leftover
    print(f'#{test_case}')
    print(*(output))