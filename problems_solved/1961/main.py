# n x n matrix를 입력받고 90도, 180도, 270도 회전을 시켜 나란히 출력한다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    size = int(input())
    output1, output2, output3 = [], [], []

    matrix = [list(map(int, input().split())) for __ in range(size)]        # input으로 size개의 행으로 이루어진 matrix 입력

    for j1 in range(size):                                                   # list new_row1에 for loop을 통해 새로운 행 요소들을 append하고 이러한 new_row를 output1 list에 append한다.
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
