
def max_adjacent_sum(matrix):
    length = len(matrix)            # 변수 초기화, 행렬 크기 저장
    maximum = 0
    temp = 0
    target = [[0]*(length+2) for _ in range(length+2)]
    for i in range(0, length):
        for j in range(0, length):
            target[i+1][j+1] = matrix[i][j]
    for x in range(1, length+1):
        for y in range(1, length+1):
            temp = target[x][y]+target[x-1][y]+target[x+1][y]+target[x][y-1]+target[x][y+1]
            if maximum < temp:
                maximum = temp
    return maximum

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]


print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
