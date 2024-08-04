T = int(input())
for test_case in range(1, T+1):
    total = list(map(int, input().split()))[0]
    passed_set = set(list(map(int, input().split())))
    failed_set = set([i for i in range(1, total+1)])
    failed_set -= passed_set
    output = []
    output.append('#'+str(test_case))
    output.extend(list(failed_set))
    print(*output)