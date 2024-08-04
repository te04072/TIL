# 인덱스가 아닌 고저차만 구하면 되므로 sort로 풀어도 무방하다

for test_case in range(1,11):   # test case 10개
    T = int(input())    # flatten 실행횟수
    boxes = list(map(int, input().split()))     # box 100개 list에 입력
    for times in range(1, T+2):  
        i = 0; maxB = 0; maxI = 0; minB = 0; minI = 0  # 초기화
        for i in range(100):    # ** T+"1"회 동안 100개에 대해 최대최소 판정 **
            if i == 0:
                maxB = boxes[0]
                minB = boxes[0]
            elif maxB < boxes[i]:
                maxB = boxes[i]
                maxI = i
            elif minB > boxes[i]:
                minB = boxes[i]
                minI = i
        if times != T+1:  # T+1번째에 대소판정만
            boxes[maxI] -= 1
            boxes[minI] += 1
    output = maxB - minB
    print(f'#{test_case} {output}')
