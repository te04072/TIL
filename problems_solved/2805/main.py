T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    target = [list(map(int, input())) for __ in range(size)]
    mid_i = size//2
    output = 0  # mid+ (2mid-i)
    for i in range(size):
        if i <= mid_i:
            for j in range(mid_i - i, mid_i + i + 1):       # mid 중심, 양쪽으로 i만큼
                output += target[i][j]
        else:
            for j in range(i - mid_i, 3 * mid_i - i + 1):   # mid 중심, 양쪽으로 2mid-i(=size-i-1) 만큼
                output += target[i][j]
    print(f"#{test_case} {output}")