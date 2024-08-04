for x in range(1, 11):
    test_case = int(input())
    matrix = [list(map(int, input().split())) for __ in range(100)]
    size = len(matrix)
    maximum = 0
    temp = 0

    for i1 in range(size): # 가로합
        temp = 0
        for j1 in range(size):
            temp += matrix[i1][j1]
        if maximum < temp:
            maximum = temp

    for j2 in range(size): # 세로합
        temp = 0
        for i2 in range(size):
            temp += matrix[i2][j2]
        if maximum < temp:
            maximum = temp

    temp = 0                    # temp 초기화 위치 항상 조심할 것
    for i3 in range(size): # 대각합
        temp += matrix[i3][i3]
    if maximum < temp:
            maximum = temp

    temp = 0
    for i4 in range(size):
        temp += matrix[i4][size-1-i4]
    if maximum < temp:
        maximum = temp

    print(f'#{test_case} {maximum}')
