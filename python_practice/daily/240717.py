# # 아래 함수를 수정하시오.
# def add_numbers(a,b):
#     return a+b
# x = 3
# y = 5
# print(f"{x}과 {y}를 인자로 넘긴 경우,\n{add_numbers(x,y)}")
# # 수정한 add_numbers() 함수를 호출하시오.

# # 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
# negative = -3
# print(abs(negative))
#
# # 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
# empty_list = []
# print(bool(empty_list))
#
# # 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))
#
# # 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
# unsorted_list = ['하', '교', '캅', '의', '지', '가']
# print(sorted(unsorted_list))

# def my_multi(number_1, number_2):
#     return number_1 * number_2
# # my_multi(2, 3) 결과 : 6
# # 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.
#
# def is_negative(number):
#     if number > 0:
#         return False
#     else:
#         return True
# # is_negative(3) 결과 : False
# # 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.
#
# def default_arg_func(default='기본 값'):
#     print(default)
#
# result_1 = my_multi(2,3)
# print(result_1)
# result_2 = is_negative(3)
# print(result_2)
# result_3 = default_arg_func()
# result_4 = default_arg_func('다른 값')

# pro_num = 1000
# global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}
#
# def create_data(subject, day, title=None):
#     data = {}
#     data['과목'] = subject
#     data['일차'] = day
#     data['제목'] = title
#     global pro_num
#     pro_num += 1
#     data['문제 번호'] = pro_num
#
#     return data
#
# result_1 = create_data('python', 3)
# result_2 = create_data('web', 1, 'web 연습하기')
# result_3 = create_data(**global_data)
# print(result_1)
# print(result_2)
# print(result_3)

# def recur_example(number):
#     if number == 1:
#         return 1
#     else:
#         return number + recur_example(number - 1)
#
#
# result_1 = recur_example(5)
# print(result_1)  # 5 + 4 + 3 + 2 + 1 = 15
#
# # 거듭 제곱 재귀 함수
# # base = 밑, exponent = 지수
# # base의 exponent승 == 2의 3승
#
#
# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     else:
#         return base*power(base, exponent-1)
#
#
# result_2 = power(2, 3)
# print(result_2)  # 2 * 2 * 2 * 1 = 8
#
# # 모든 자릿수 더하기 함수
#
#
# def sum_of_digits(number):
#     if number < 10:
#         return number
#     else:
#         return sum_of_digits(number % 10) + sum_of_digits(number//10)
#
#
# result_3 = sum_of_digits(321)
# print(result_3)  # 1 + 2 + 3 = 6

# number_of_people = 0
#
#
# def increase_user():
#     global number_of_people
#     number_of_people += 1
#
#
# increase_user()
# print(f"현재 가입 된 유저 수 : {number_of_people}")

# number_of_people = 0
#
#
# def increase_user():
#     global number_of_people
#     number_of_people += 1
#     pass
#
#
# def create_user(name, age, address):
#     print(f"{name}님 환영합니다!")
#     user_info = {'name': name, 'age': age, 'address': address}
#     increase_user()
#     return user_info
#
#
# print(f"현재 가입 된 유저 수 : {number_of_people}")
# print(create_user('홍길동', 30, '서울'))
# print(f"현재 가입 된 유저 수 : {number_of_people}")

# def rental_book(name, number):
#     decrease_book(number)
#     print(f"{name}님이 {number}권의 책을 대여하였습니다.")
#
#
# number_of_book = 100
#
#
# def decrease_book(rented_book):
#     global number_of_book
#     number_of_book -= rented_book
#     print(f"남은 책의 수 : {number_of_book}")
#
# rental_book('홍길동', 3)

# number_of_people = 0
#
#
# def increase_user():
#     pass
#
#
# def create_user(user_name, user_age, user_address):
#     print(f"{user_name}님 환영합니다!")
#     user_info = {'name': user_name, 'age': user_age, 'address': user_address}
#     increase_user()
#     return user_info
#
#
# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']
#
# print(list(map(create_user, name, age, address)))


number_of_people = 0
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(user_name, user_age, user_address):
    print(f"{user_name}님 환영합니다!")
    user_info = {'name': user_name, 'age': user_age, 'address': user_address}
    return user_info


many_user = list(map(create_user, name, age, address))

def decrease_book(rented_book):
    global number_of_book
    number_of_book -= rented_book
    print(f"남은 책의 수 : {number_of_book}")


def rental_book(info):
    rented_book = info['age'] // 10
    decrease_book(rented_book)
    print(f"{info['name']}님이 {rented_book}권의 책을 대여하였습니다.")


info_list = list(map(lambda item: {'name': item['name'], 'age': item['age']}, many_user))
list(map(rental_book, info_list))