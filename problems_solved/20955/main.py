T = int(input())
for test_case in range(1, T+1):
    S = input()
    E = input()
    output = 'No'
    while len(E) != len(S):
        if E[-1] == 'X':
            E = E[0:-1]
        else:
            E = E[0:-1]
            E = E[::-1]
    if S == E:
        output = 'Yes'
    print(f"#{test_case} {output}")
