import math


def solution(fees, records):
    answer = []
    gate = []
    fee_dict = {}
    for rec in records:
        if rec[-2:] == "IN":                        # 차량 번호 및 진입시간 기록
            gate.append(rec[0:-3])
        else:
            car_num = rec[6:-4]
            for car in gate:
                if car_num in car:                  # 나가는 차량의 진입시간 확인 후 dict에 누적시간 갱신
                    time = time_calc(car[:5], rec[:5])
                    val = fee_dict.get(car_num, 0)
                    val += time
                    fee_dict.update({car_num: val})
                    gate.remove(car)
                    break
    if gate:
        for car in gate:                            # 나간 시간이 기록되지 않은 경우 23:59로 계산
            car_num = car[6:]
            time = time_calc(car[:5], '23:59')
            val = fee_dict.get(car_num, 0)
            val += time
            fee_dict.update({car_num: val})
    car_list = sorted(fee_dict.keys())
    for car in car_list:
        answer.append(fee_calc(fees, fee_dict[car]))    # 주차요금 계산하여 차량번호 순으로 저장
    return answer


def time_calc(start, end):
    hour = int(end[:2]) - int(start[:2])
    min = int(end[-2:]) - int(start[-2:])
    if min < 0:
        hour -= 1
        min += 60
    return min + hour * 60


def fee_calc(ls, time):
    if time <= ls[0]:
        return ls[1]
    else:
        return ls[1] + math.ceil((time - ls[0]) / ls[2]) * ls[3]


fee = list(map(int, input().split(",")))
string = input().strip('"')
record = list(string.split('", "'))
print(solution(fee, record))
