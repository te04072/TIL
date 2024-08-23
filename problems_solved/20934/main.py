T = int(input())
for test_case in range(1, T+1):
    string, K = input().split()
    for i in range(3):
        if string[i] == 'o':
            cur = i
    for __ in range(int(K)):
        if cur == 0 or cur == 2:
            cur = 1
        elif cur == 1:
            cur = 0
    print(f"#{test_case} {cur}")
