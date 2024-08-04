def is369(x):
    if x != 0 and x % 3 == 0:
        return 1
    else:
        return 0


num = int(input())
for i in range(1, num+1):
    a = i / 100
    b = (i // 10) % 10
    c = i % 10
    count = is369(a) + is369(b) + is369(c)
    if count > 0:
        print("-"*count, end=' ')
    else:
        print(i, end=' ')
