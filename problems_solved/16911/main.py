T = int(input())
for test_case in range(1, T+1):
    length = int(input())
    target = list(map(int, input().split()))
    # count_list = [0]*10**6
    # for i in range(length):
    #     count_list[target[i]] += 1
    max_even_i = 0
    max_odd_i = 1
    max_even_i2 = 0
    max_odd_i2 = 1
    for i in range(length):
        if i % 2 == 0:
            if target[max_even_i] < target[i]:
                max_even_i = i
        else:
            if target[max_odd_i] < target[i]:
                max_odd_i = i
    ans1 = target[max_even_i] + target[max_odd_i]
    if target[max_even_i] == target[max_odd_i]:
        for i in range(length):
            if i % 2 == 0:
                if target[max_even_i2] < target[i] < target[max_even_i]:
                    max_even_i2 = i
            else:
                if target[max_odd_i2] < target[i] < target[max_odd_i]:
                    max_odd_i2 = i
        ans2 = target[max_even_i] + target[max_even_i2] + target[max_odd_i2]
        if ans1 > ans2:
            print(f'#{test_case} {ans2}')
    else: print(f'#{test_case} {ans1}')