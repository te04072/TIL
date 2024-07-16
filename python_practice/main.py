import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    output1, output2, output3 = [], [], []

    matrix = [list(map(int, input().split())) for __ in range(size)]

    for j1 in range(size):
        new_row1 = []
        for i1 in range(size):
            new_row1.append(matrix[size-i1-1][j1])
        output1.append(new_row1)

    for i2 in range(size):
        new_row2 = []
        for j2 in range(size):
            new_row2.append(matrix[size-i2-1][size-j2-1])
        output2.append(new_row2)

    for i3 in range(size):
        new_row3 = []
        for j3 in range(size):
            new_row3.append(matrix[j3][size-i3-1])
        output3.append(new_row3)

    print(f'#{test_case}')
    for count in range(size):
        print(''.join(map(str, output1[count])), ''.join(map(str, output2[count])), ''.join(map(str, output3[count])))
