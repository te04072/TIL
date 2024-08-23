import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    size = int(input())
    target = [list(map(int, input().split())) for __ in range(size)]
    status = None
    thresholds = [0]*(size+1)
    stack = []
    for i in range(size):
        for j in range(size):
            cur = bool(target[i][j])
            if not status and cur:                               # 연속되지 않은 새로운 행렬 발견
                stack.append(j)
            elif cur and j == 0:
                stack.append(j)                                 # 행의 시작점에서 행렬이 시작할 때도 append
            elif status and not cur:                            # 용기의 연속성 끊겼을 때
                thresholds[j - stack.pop()] += 1                # 행 인덱스에 열 길이 추가
            elif status and cur and j == (size-1):              # 행의 마지막에서 행렬이 끝날 때도 pop
                thresholds[j + 1 - stack.pop()] += 1
            status = bool(target[i][j])                         # 다음 요소와 비교할 boolean 저장
    for k in range(size+1):
        if thresholds[k]:
            stack.append([thresholds[k], k])                    # 행과 열의 쌍을 열 순서대로 저장, 이후 스택은 그냥 리스트로 사용
    for m in range(len(stack)):
        for n in range(len(stack)-1-m):                         # 넓이가 크면서 행 길이가 더 긴 경우에만 뒷 순서로 정렬
            if stack[n][0]*stack[n][1] >= stack[n+1][0]*stack[n+1][1] and stack[n][0] > stack[n+1][0]:
                stack[n], stack[n+1] = stack[n+1], stack[n]
            # if stack[n][0]*stack[n][1] > stack[n+1][0]*stack[n+1][1] or (
            #         stack[n][0]*stack[n][1] > stack[n+1][0]*stack[n+1][1] and stack[n][0] > stack[n+1][0]):
            #     stack[n], stack[n+1] = stack[n+1], stack[n]
    print(f"#{test_case} {len(stack)}", end=' ')
    for x in range(len(stack)):
        print(*stack[x], end=' ')
    print()
