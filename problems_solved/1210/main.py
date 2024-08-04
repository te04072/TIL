def direc_check(ls, pos):
    if pos == 0:
        if ls[pos+1] == 1:
            return 'right'
    elif pos == len(ls) - 1:
        if ls[pos-1] == 1:
            return 'left'
    elif ls[pos + 1] == 1:
        return 'right'
    elif ls[pos - 1] == 1:
        return 'left'
    else:
        return 'go'


def move_check(ls, pos, direc):
    while (0 <= pos+direc <= 99) and ls[pos+direc] == 1:
        pos += direc
    return pos

    # while (0 <= pos+direc <= 99) and ls[pos+direc] == 1:       #이 코드는 왜 진동하는가
    #     pos += direc
    #     if pos == 0 or 99:
    #         break


for test_case in range(1, 11):
    T = int(input())
    target = [list(map(int, input().split())) for __ in range(100)]
    start_j = 0
    ans_j = 0
    for x in range(100):
        if target[99][x] == 2:
            start_j = x

    cur = start_j
    for m in range(98, -1, -1):
        print(cur)
        if direc_check(target[m], cur) == 'right':
            cur = move_check(target[m], cur, 1)
        elif direc_check(target[m], cur) == 'left':
            cur = move_check(target[m], cur, -1)
        else:
            continue
    ans_j = cur
    print(f'#{test_case} {ans_j}')