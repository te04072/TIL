# list_of_book = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]
#
# rental_list = [
#     '장생전',
#     '원생몽유록',
#     '이생규장전',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]
# rent_count = 0
# for i in range(len(rental_list)):
#     count = -1
#     while count < len(list_of_book)-1:
#         if list_of_book[count] == rental_list[i]:
#             rent_count += 1
#             break
#         else:
#             count += 1
#     if count == len(list_of_book)-1:
#         print(f'{rental_list[i]} 은/는 보유하고 있지 않습니다.')
#
# if rent_count == len(rental_list):
#     print('모든 도서가 대여 가능한 상태입니다.')

# list_of_book = [
#     '장화홍련전',
#     '가락국 신화',
#     '온달 설화',
#     '금오신화',
#     '이생규장전',
#     '만복자서포기',
#     '수성지',
#     '백호집',
#     '원생몽유록',
#     '홍길동전',
#     '장생전',
#     '도문대작',
#     '옥루몽',
#     '옥련몽',
# ]
#
# rental_book = [
#     '장생전',
#     '위대한 개츠비',
#     '원생몽유록',
#     '이생규장전',
#     '데미안',
#     '장화홍련전',
#     '수성지',
#     '백호집',
#     '난중일기',
#     '홍길동전',
#     '만복자서포기',
# ]
#
# rent_count = 0
# for i in range(len(rental_book)):
#     count = -1
#     while count < len(list_of_book)-1:
#         if list_of_book[count] == rental_book[i]:
#             rent_count += 1
#             break
#         else:
#             count += 1
#     if count == len(list_of_book)-1:
#         missing_book = [rental_book[i] for i in range(len(rental_book))]
#         print(f'{rental_book[i]} 을/를 보충하여야 합니다.')
#
# if rent_count == len(rental_book):
#     print('모든 도서가 대여 가능한 상태입니다.')

# food_list = [
#     {
#         '종류': '한식',
#         '이름': '잡채'
#     },
#     {
#         '종류': '채소',
#         '이름': '토마토'
#     },
#     {
#         '종류': '중식',
#         '이름': '자장면'
#     },
# ]

# for i in range(len(food_list)):
#     if food_list[i]['이름'] == '토마토':
#         food_list[i]['종류'] = '과일'
#     elif food_list[i]['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
#     print(f"{food_list[i]['이름']} 은/는 {food_list[i]['종류']} (이)다.")
#
# print(food_list)

# i = 0
# while i < len(food_list):
#     if food_list[i]['이름'] == '토마토':
#         food_list[i]['종류'] = '과일'
#     elif food_list[i]['이름'] == '자장면':
#         print('자장면엔 고춧가루지')
#     print(f"{food_list[i]['이름']} 은/는 {food_list[i]['종류']} (이)다.")
#     i += 1
#
# print(food_list)

# matrix = [
#         ['0, 1', '0, 2', '0, 3'],
#         ['1, 0', '1, 1', '1, 2', '1, 3'],
#         ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'],
#         ['3, 0', '3, 1'],
#         ['4, 0', '4, 1', '4, 2'],
#         ['5, 0']
#     ]
# matrix_len = 0
# for index_0, number_0 in enumerate(matrix):
#     matrix_len += 1
# print(matrix_len)
#
# for index, number in enumerate(matrix):
#     temporary_len = 0
#     for index_i, numbers in enumerate(number):
#         temporary_len += 1
#     if temporary_len < 5:
#         print(f"{number} 리스트는 {temporary_len}개 만큼 요소를 가지고 있습니다.")
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(f"matrix의 {i}, {j} 번째 요소의 값은 {matrix[i][j]} 입니다.")

# import requests
# from pprint import pprint as print
#
# dummy_data = []
# # 무작위 유저 정보 요청 경로
# # API 요청
# for i in range(1,11):
#     API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
#     response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
#     parsed_data = response.json()
#     name = parsed_data['name']
#     lat = parsed_data['address']['geo']['lat']
#     lng = parsed_data['address']['geo']['lng']
#     company = parsed_data['company']['name']
#     if -80< float(lat) < 80 and -80 < float(lng) < 80:
#         dummy_data.append({'company': company, 'lat': lat, 'lng': lng, 'name': name})
#
# print(dummy_data)

# black_list = [
#     'Hoeger LLC',
#     'Keebler LLC',
#     'Yost and Sons',
#     'Johns Group',
#     'Romaguera-Crona',
# ]
#
#
# import requests
# from pprint import pprint as print
#
# company_dict = {}
# # 무작위 유저 정보 요청 경로
# # API 요청
# for i in range(1,11):
#     API_URL = 'https://jsonplaceholder.typicode.com/users/'+str(i)
#     response = requests.get(API_URL)
# # JSON -> dict 데이터 변환
#     parsed_data = response.json()
#     name = parsed_data['name']
#     lat = parsed_data['address']['geo']['lat']
#     lng = parsed_data['address']['geo']['lng']
#     company = parsed_data['company']['name']
#     if -80< float(lat) < 80 and -80 < float(lng) < 80:
#         company_dict[company] = name
#
# censored_user_list = {}
# def create_user(user_dict):
#      for company_key, user_value in user_dict.items():
#         if censorship(company_key, user_value) == True:
#             censored_user_list[company_key] = [user_value]
#
# def censorship(user_company, user):
#     for i in range(len(black_list)):
#         if user_company == black_list[i]:
#             print(f'{user_company}의 {user} 은/는 등록할 수 없습니다.')
#             return False
#             break
#         elif i == len(black_list)-1:
#             print('이상 없습니다.')
#             return True
#         else:
#             i += 1
#
# create_user(company_dict)
# print(censored_user_list)

user_data = [
    {
        'blood_group': 'AB',
        'company': 'Stone Inc',
        'mail': 'ian17@yahoo.com',
        'name': 'Kathryn Jenkins',
        'website': [
            'https://www.boyd-herrera.com/',
            'https://watson.com/',
            'http://www.mitchell.com/',
            'http://irwin-cline.biz/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fleming Ltd',
        'mail': 'patricianelson@yahoo.com',
        'name': 'Angel Williamson',
        'website': [
            'https://wilson-johnson.com/',
            'https://santiago-hammond.com/',
            'https://morales.com/',
            'https://fry-fleming.com/',
        ],
    },
    {
        'blood_group': 'A+',
        'company': 'Scott PLC',
        'mail': 'lisajones@gmail.com',
        'name': 'Stephanie Herman MD',
        'website': [
            'https://www.boyer-stevens.org/',
            'http://www.johnson.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Warren-Stewart',
        'mail': 'allisonjennifer@gmail.com',
        'name': 'Jon Martinez',
        'website': ['https://www.berg.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Fisher Inc',
        'mail': 'mross@yahoo.com',
        'name': 'Justin Brown',
        'website': [
            'https://www.gray.com/',
            'https://jones.com/',
            'http://williams.biz/',
            'https://hammond.net/',
        ],
    },
    {
        'blood_group': 'B-',
        'company': 'Pearson Group',
        'mail': 'gravesbarbara@hotmail.com',
        'name': 'Bobby Patterson',
        'website': ['https://www.cunningham.biz/', 'https://johnson.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'White, Andrade and Howard',
        'mail': 'mcole@gmail.com',
        'name': 'Michelle Strickland',
        'website': ['http://www.rose-gomez.com/', 'https://reilly.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Young',
        'mail': 'tmorales@hotmail.com',
        'name': 'Stephanie Moore',
        'website': ['https://schmidt.com/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Brooks PLC',
        'mail': 'wellsmatthew@hotmail.com',
        'name': 'Dr. David Johnson',
        'website': [
            'http://ford-dean.com/',
            'http://www.petersen.com/',
            'https://thompson-cooley.info/',
            'http://ryan-gay.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Stewart Group',
        'mail': 'sean37@hotmail.com',
        'name': 'Veronica Webb',
        'website': ['http://www.holmes.info/', 'http://www.morris.biz/'],
    },
    {
        'blood_group': 'AB+',
        'company': 'Cabrera, Perry and Harris',
        'mail': 'bgonzales@yahoo.com',
        'name': 'Lisa Wilcox',
        'website': ['https://www.small.com/', 'http://martin-petersen.com/'],
    },
    {
        'blood_group': 'B+',
        'company': 'Thomas, Lozano and Lopez',
        'mail': 'bperry@yahoo.com',
        'name': 'Brian Simmons',
        'website': [
            'http://reid.com/',
            'http://www.roman-neal.biz/',
            'https://www.hoover.org/',
            'https://www.lynn.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Baker-Leach',
        'mail': 'johnlucas@yahoo.com',
        'name': 'Carlos Robinson',
        'website': ['https://martin.com/', 'http://montgomery-cline.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Higgins, Higgins and Garcia',
        'mail': 'chris66@gmail.com',
        'name': 'Gabriel Collins',
        'website': ['https://www.cole-pugh.com/'],
    },
    {
        'blood_group': 'AB-',
        'company': 'Tanner, Wheeler and Weaver',
        'mail': 'leonardtammy@gmail.com',
        'name': 'Christopher Cook',
        'website': [
            'https://www.myers-reynolds.com/',
            'https://dunlap-rogers.com/',
            'https://luna.net/',
            'http://smith-miller.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Schaefer-Hunter',
        'mail': 'nsummers@gmail.com',
        'name': 'Daniel Monroe',
        'website': [
            'https://cook.net/',
            'http://carpenter.com/',
            'http://morris-terrell.com/',
        ],
    },
    {
        'blood_group': 'B+',
        'company': 'Stephens Group',
        'mail': 'rolson@gmail.com',
        'name': 'Molly Parks',
        'website': [
            'https://wright-vincent.biz/',
            'http://www.cruz.com/',
            'http://olson.org/',
            'http://gomez.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Fitzgerald, Costa and Hobbs',
        'mail': 'jennifervang@hotmail.com',
        'name': 'Jill Patterson',
        'website': [
            'https://www.brewer.com/',
            'https://malone-murray.info/',
            'http://evans.com/',
            'https://ortiz.com/',
        ],
    },
    {
        'blood_group': 'A-',
        'company': 'Frazier Ltd',
        'mail': 'vsolis@hotmail.com',
        'name': 'Marie May',
        'website': [
            'http://pratt.info/',
            'http://www.ortega.com/',
            'http://www.smith.net/',
            'https://nichols.biz/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Rodriguez and Sons',
        'mail': 'michael09@yahoo.com',
        'name': 'Julia Gonzalez',
        'website': [
            'https://www.cantrell.com/',
            'https://www.smith.net/',
            'http://delgado.com/',
            'http://stevens.com/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Brown-Arnold',
        'mail': 'christopher79@hotmail.com',
        'name': 'David Garza',
        'website': ['https://price.net/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Butler-Hernandez',
        'mail': 'angiechoi@yahoo.com',
        'name': 'Leslie Kemp',
        'website': ['http://www.martin-thompson.org/', 'http://martin.org/'],
    },
    {
        'blood_group': 'A-',
        'company': 'Schneider-Hensley',
        'mail': 'cesarsantos@hotmail.com',
        'name': 'Brandon Peterson',
        'website': [
            'https://www.owens-gay.com/',
            'https://www.santiago.org/',
            'https://www.singleton.com/',
        ],
    },
    {
        'blood_group': 'O-',
        'company': 'Hunter, Alvarado and Stewart',
        'mail': 'thomas16@gmail.com',
        'name': 'Matthew Stanley',
        'website': ['https://nelson.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Elliott, Mullins and Michael',
        'mail': 'smithedward@hotmail.com',
        'name': 'Robert Brown',
        'website': [
            'http://montgomery-rogers.biz/',
            'http://www.williams-nixon.com/',
        ],
    },
    {
        'blood_group': 'AB+',
        'company': 'Velasquez-Garcia',
        'mail': 'samanthawilson@yahoo.com',
        'name': 'Stephanie Cohen',
        'website': ['http://jackson-harris.com/'],
    },
    {
        'blood_group': 'A+',
        'company': 'Mccoy-Hopkins',
        'mail': 'lli@yahoo.com',
        'name': 'Michael Clark',
        'website': [
            'https://www.harding.info/',
            'https://www.jones.biz/',
            'http://knight-adkins.org/',
            'http://www.alvarado-mendoza.org/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Kerr Ltd',
        'mail': 'georgebrittany@yahoo.com',
        'name': 'Brandon White',
        'website': [
            'https://flowers-parker.info/',
            'http://oliver-rice.info/',
        ],
    },
    {
        'blood_group': 'AB-',
        'company': 'Villarreal, Wood and Smith',
        'mail': 'denise73@yahoo.com',
        'name': 'Kevin Blevins',
        'website': [
            'http://www.ramirez.info/',
            'https://mckay.net/',
            'http://duran.com/',
        ],
    },
    {
        'blood_group': 'O+',
        'company': 'Jenkins-Garcia',
        'mail': 'kwoodward@hotmail.com',
        'name': 'Michelle Dixon',
        'website': [
            'http://www.taylor.com/',
            'https://bates-trujillo.org/',
            'https://www.thomas-boyer.org/',
        ],
    },
]

blood_types = ['A-', 'A+', 'B-', 'B+', 'O-', 'O+', 'AB-', 'AB+']
black_list = [
    'Jenkins-Garcia',
    'Stephens Group',
    'White, Andrade and Howard',
    'Warren-Stewart',
]

# user_data [{}{}{}{}}
#
#
# user_list = []
# false_count = 0


# def create_user(user_data_0):
#     global false_count
#     for i in range(len(user_data_0)):
#         result = is_validation(user_data_0[i])
#         if result == 'blocked':
#             false_count += 1
#         elif result is not True:
#             false_count += 1
#             user_list.append(result)
#         else:
#             user_list.append(result)
#     print(f'잘못된 데이터로 구성된 유저의 수는 {false_count} 입니다.')
#
# def is_validation(user_info):
#     temp_list = []
# #    for __ in range(len(user_info)):
#     if list_check(user_info.get['blood_group'], blood_types) is not True:
#         user_info['blood_group'] = None
#         temp_list.append('blood_group')
#     if list_check(user_info.get['company'], black_list) is True:
#         temp_list.append('company')
#         return 'blocked'
#     if list_check('@', list(user_info.get['mail'])) is not True:
#         user_info['mail'] = None
#         temp_list.append('mail')
#     if (2 <= len(user_info.get['name']) <= 30) is not True:
#         user_info['name'] = None
#         temp_list.append('name')
#     if (1 <= len(user_info.get['website'])) is not True:
#         user_info['website'] = None
#         temp_list.append('website')
#     if len(temp_list) == 0:
#         return True
#     else:
#         return False, temp_list
#
#
# def list_check(target, list_a):
#     for k in range(len(list_a)):
#         if target == list_a[k]:
#             return True
#         elif k == len(list_a)-1:
#             return False
#         else:
#             k += 1
#

user_list = []
false_count = 0


def create_user(u_list):
    global false_count
    for i in range(len(u_list)):
        result = is_validation(u_list[i])
        if result == 'blocked':
            false_count += 1
        elif result == True:
            user_list.append(u_list[i])
        else:
            if 'blood_group' in result[1]:
                u_list[i]['blood_group'] = None
            if 'mail' in result[1]:
                u_list[i]['mail'] = None
            if 'name' in result[1]:
                u_list[i]['name'] = None
            if 'website' in result[1]:
                u_list[i]['website'] = None
            user_list.append(u_list[i])
            false_count += 1
    print({f'잘못된 데이터로 구성된 유저의 수는 {false_count}입니다.'})
    print(user_list)


def is_validation(u_info):
    temp_list = []
    if (u_info['blood_group'] in blood_types) is not True:
        temp_list.append('blood_group')
    if (u_info['company'] in black_list) is True:
        return 'blocked'
    if ('@' in u_info['mail']) is not True:
        temp_list.append('mail')
    if (2 <= len(u_info['name']) <= 30) is not True:
        temp_list.append('name')
    if (len(u_info['website']) >= 1) is not True:
        temp_list.append('website')
    if len(temp_list) == 0:
        return True
    else:
        return False, temp_list


create_user(user_data)
print(is_validation(user_list[0]))
