# T = int(input())
# for test_case in range(1, T+1):
#     total = list(map(int, input().split()))[0]
#     passed_set = set(list(map(int, input().split())))
#     failed_set = set([i for i in range(1, total+1)])
#     failed_set -= passed_set
#     output = []
#     output.append('#'+str(test_case))
#     output.extend(list(failed_set))
#     print(*output)

T = int(input())
for test_case in range(1, T+1):
    total, passed_num = map(int, input().split())
    passed_list = list(map(int, input().split()))

    failed_list = []
    for i in range(1, total+1):
        if (i in passed_list) is False:
            failed_list.append(i)
        else:
            pass
    print(f"#{test_case} {' '.join(map(str, failed_list))}")             # 출력 연습