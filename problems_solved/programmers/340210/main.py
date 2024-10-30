def dec_to_n(num, d):                                   # 출력용: n진법 반환
    string = ''
    num = int(num)
    if num == 0:
        return 0
    else:
        while num:
            string += str(num % d)
            num //= d
        string = int(string[::-1])
    return string

def n_to_dec(num, d):                                   # 연산용: 10진법 반환
    res = 0
    string = str(num)
    for i in range(len(string)):
        res += int(string[i]) * d **(len(string) - i - 1)
    return res


def solution(expressions):
    answer = []
    digit_l = 2                                         # 최소 2진법에서 시작
    digits = []
    visited = []
    
    for exp in expressions:
        for c in exp:   
            if c.isnumeric():                           # 먼저 전체 식을 순회하며 최소 몇진수인지 확인
                digit_l = max(digit_l, int(c)+1)
    for exp in expressions:
        cur_num = ''
        nums = []
        calc = ''
        if exp[-1] != 'X':                                  # 계산 가능한 수식들만
            for c in exp:
                if c == ' ':
                    continue
                if c.isnumeric():                           # 스트링에 숫자 저장
                    cur_num += c
                else:                                       # 연산자가 나타나면 숫자 append
                    if c != '=':
                        calc = c
                    if cur_num:
                        nums.append(cur_num)
                        cur_num = ''
            if cur_num:
                nums.append(cur_num)
                cur_num = ''

            for d in range(digit_l, 10):                    # 최소 진법에서 9진법까지 순회
                num1 = n_to_dec(nums[0], d)
                num2 = n_to_dec(nums[1], d)
                num3 = n_to_dec(nums[2], d)                
                if calc == '+':
                    temp = num1 + num2
                else:
                    temp = num1 - num2
                if temp == num3:                # 수식을 만족시키는 진법 발견시 append
                    if d not in digits and d not in visited:
                        digits.append(d)
                else:
                    if d in digits: 
                        digits.remove(d)
                        visited.append(d)           # 수식 하나라도 반례 나오면 목록에서 제거
    for exp in expressions:
        nums = []
        cur_num = ''
        calc = ''
        a = ''
        new_a = ''
    
        if exp[-1] == 'X':
            if not digits:                          # 모두 미지수인 케이스
                new_exp = exp[:-1] + '?'
            else:
                exp = exp[:-1]
                for d in digits:                    # 최소 진법에서 9진법까지 순회
                    for c in exp:
                        if c == ' ':
                            continue
                        if c.isnumeric():                           # 스택에 숫자 저장
                            cur_num += c
                        else:                                       # 연산자가 나타나면 스택의 숫자 계산하여 저장
                            if c != '=':
                                calc = c
                            if cur_num:
                                nums.append(cur_num)
                                cur_num = ''
                    num1 = n_to_dec(nums[0], d)
                    num2 = n_to_dec(nums[1], d)                
                    if calc == '+':
                        temp = num1 + num2
                    else:
                        temp = num1 - num2
                    new_a = str(dec_to_n(temp, d))
                    if a == '':
                        a = new_a
                    else:
                        if new_a != a:
                            new_exp = exp + '?'
                            break
                else:
                    new_exp = exp + new_a                           # 수식 결과가 모두 일치하면 정답을 붙임
            answer.append(new_exp)
    return answer

print(solution(["14 + 3 = 17", "13 - 6 = X", "51 - 5 = 44"]))