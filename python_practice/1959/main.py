T = int(input()) # 2개의 숫자열을 순서대로 대응시킨 숫자쌍의 곱들의 합의 최댓값
for test_case in range(1, T + 1):
    length = list(map(int, input().split()))
    M = list(map(int, input().split()))
    N = list(map(int, input().split()))
    output = 0
    if length[0] < length[1]:
        (M, N) = (N, M)
    sum_list = [0] * (len(M) - len(N)+1)   # sum_list = [] 시 index error
    for i in range(len(M)-len(N)+1):
        for j in range(len(N)):
            sum_list[i] += M[i+j] * N[j]   # append 사용?
        if i == 0:
            output = sum_list[0]
        else:
            if output < sum_list[i]:
                output = sum_list[i]
    print(f'#{test_case} {output}')
