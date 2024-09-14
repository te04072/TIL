# N = int(input())                                                # 스위치 수
# switches = list(map(int, input().split()))                      # 스위치 번호는 1번부터인 것에 주의
# n = int(input())                                                # 학생 수
# students = [list(map(int, input().split())) for __ in range(n)]
# for i in range(n):
#     x = students[i][1]                                           # 각 학생이 받은 수
#     if students[i][0] == 1:                                      # 남학생
#         for j in range(N//x):
#             switches[x*(j+1)-1] += 1                             # x의 배수인 스위치 누르기
#     else:                                                        # 여학생
#         t = 0
#         while (0 <= x-t-1 < N) and (0 <= x-1+t < N):             # 인덱스 범위 내에서 x 기준 스위치 상태 확인
#             if switches[x-1+t] % 2 == switches[x-1-t] % 2:
#                 t += 1
#             else:
#                 break
#         if t > 0:
#             t -= 1
#         for j in range(x-t-1, x+t):
#             switches[j] += 1
# for k in range(N):
#     if (k + 1) % 20 == 0:
#         print(switches[k]%2, end='\n')
#     else:
#         print(switches[k]%2, end=' ')

def toggle_switch(state):
    if state == 0:
        return 1
    else:
        return 0


N = int(input().strip())
switches = list(map(int, input().strip().split()))
s_cnt = int(input().strip())

for _ in range(s_cnt):
    gender, s_num = map(int, input().strip().split())
    s_i = s_num - 1

    if gender == 1:
        for i in range(s_i, len(switches), s_num):
            switches[i] = toggle_switch(switches[i])
    else:
        t_range = 0

        for i in range(1, len(switches)):
            if 0 <= s_i - i and s_i + i < len(switches):
                if switches[s_i - i] == switches[s_i + i]:
                    t_range += 1
                else:
                    break

        if t_range == 0:
            switches[s_i] = toggle_switch(switches[s_i])
        else:
            for i in range(s_i - t_range, s_i + t_range + 1):
                switches[i] = toggle_switch(switches[i])

print_cnt = len(switches) // 20
print_rest = len(switches) % 20

if print_rest > 0:
    print_cnt += 1

for p_cnt in range(print_cnt - 1):
    print(" ".join(map(str, switches[p_cnt * 20: p_cnt * 20 + 20])).strip())
else:
    if print_rest:
        print(" ".join(map(str, switches[(len(switches) // 20) * 20:])).strip())
