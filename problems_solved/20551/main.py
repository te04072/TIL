T = int(input())
for test_case in range(1, T+1):
    target = list(map(int, input().split()))
    output = 0
    for i in range(2, 0, -1):
        if target[i] <= target[i-1]:
            output += target[i-1] - target[i] + 1
            target[i-1] -= output
    if target[0] < 1:
        output = -1
    print(f"#{test_case} {output}")