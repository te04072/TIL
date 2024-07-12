#정수를 input으로 받아 각 자릿수의 합을 출력하는 코드

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    while N > 0:
        sum = 0
        sum += N % 10
        N //= 10
        print(sum)



    # ///////////////////////////////////////////////////////////////////////////////////
