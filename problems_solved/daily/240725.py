# def check_number():
#     try:
#         while True:
#             x = int(input("숫자를 입력하세요: "))
#             if x > 0:
#                 print("양수입니다.")
#             elif x == 0:
#                 print("0입니다.")
#             else :
#                 print("음수입니다.")
#     except ValueError:
#         print("잘못된 입력입니다.")


# check_number()


                                        ## keyerror 발생 이유???
# class UserInfo:
#     def __init__(self):
#         self.user_data = {}
        
#     def get_user_info(self):
#         try:
#             x = str(input("이름을 입력하세요 : "))
#             self.user_data["이름"] = x
#             y = int(input("나이를 입력하세요 : "))
#             self.user_data["나이"] = y
#         except KeyError:
#             print("나이는 숫자로 입력해야 합니다.")
#         except ValueError:
#             print("나이는 숫자로 입력해야 합니다.")

#     def display_user_info(self):
#         try:
#             print(f'사용자 정보 : \n이름 : {self.user_data["이름"]} \n나이 : {self.user_data["나이"]}')
#         except KeyError:
#             print("사용자 정보가 입력되지 않았습니다.")
#         except ValueError:
#             print("사용자 정보가 입력되지 않았습니다.")


# user = UserInfo()
# user.get_user_info()
# user.display_user_info()

# data = {'name': '홍길동'}
# try:
#     if not data['age']:
#         print(data['age'])
# except KeyError:
#     print('data에는 age라는 키가 없습니다.')
#     data['age'] = 30
#     print(data)



# arr = ['반갑', '하세요', '안녕']
# try:
#     for i in range(4):
#         print(arr.pop())
# except IndexError:
#     print(arr)
#     print('더 이상 pop 할 수 없습니다.')


# word = '3.15'
# try:
#     print(int(word))
# except ValueError:
#     print('정수로 변환 가능한 값을 입력해주세요.')


# class BaseModel:
#     PK = 1
#     TYPE = 'Basic Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         self.PK = BaseModel.PK
#         self.data_type = data_type 
#         self.title = title 
#         self.content = content 
#         self.created_at = created_at 
#         self.updated_at = updated_at
#         BaseModel.PK += 1
    
#     def save(self):
#         print('데이터를 저장합니다.')

# class Novel(BaseModel):
#     def __init__(self, data_type, title, content, created_at, updated_at, author):
#         super().__init__(data_type, title, content, created_at, updated_at)
#         self.author = author
    

# class Other(BaseModel):
#     TYPE = 'Other Model'

#     def __init__(self, data_type, title, content, created_at, updated_at):
#         super().__init__(data_type, title, content, created_at, updated_at)
        
#     def save(self):
#         print('데이터를 다른 장소에 저장합니다.')

    
# class ExtendedModel(Novel, Other):
#     def __init__(self, extended_type):
#         self.extended_type = extended_type
    
#     def save(self):
#         print('데이터를 확장해서 저장합니다.')

#     def display_info(self):
#         print(f'PK: {self.PK}, TYPE: {self.TYPE}, Extended Type: {self.extended_type}')

# hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
# chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
# print('Novel 모델 인스턴스의 PK와 save 메서드')
# print(hong.PK)
# print(chun.PK)
# hong.save()
# chun.save()
# print(hong.author)
# print(chun.author)
# print('---')

# company = Other('회사', '회사명', '회사 설명', 2000, 2023)
# print('Other 모델 인스턴스의 PK와 save 메서드')
# print(company.PK)
# company.save()

# print('---')
# print('모델 별 타입')
# print(Novel.TYPE)
# print(Other.TYPE)

# extended_instance = ExtendedModel("Extended Type")
# print('ExtendedModel 인스턴스의 정보 출력 및 저장 메서드 호출')
# extended_instance.display_info()
# extended_instance.save()


# class Animal:
#     num_of_animal = 0

#     def __init__(self):
#         self.num_of_animal += 1


# class Dog(Animal):
#     def __init__(self):
#         self.num_of_animal = Animal.num_of_animal
#         Animal.num_of_animal += 1
    
#     def bark(self):
#         print('멍멍 !')


# class Cat(Animal):
#     def __init__(self, name):
#         self.num_of_animal = Animal.num_of_animal
#         self.name = name
#         Animal.num_of_animal += 1
#     def meow(self):
#         print('야옹 !')



# class Pet(Dog, Cat):

#     @classmethod
#     def __init__(self, sound):
#         self.num_of_animal = Animal.num_of_animal
#         self.sound = sound
#         Animal.num_of_animal += 1

#     def access_num_of_animal(self):
#         self.num_of_animal = Animal.num_of_animal
#         return f"동물의 수는 {self.num_of_animal}마리 입니다."
    
#     def make_sound(self):
#         print(self.sound)


#     def play(self):
#         print("애완동물과 놀기")


# dog = Dog()
# print(Pet.access_num_of_animal())
# cat = Cat()
# print(Pet.access_num_of_animal())

# dog1 = Dog()
# dog1.bark()
# cat1 = Cat("야옹")
# cat1.meow()

# pet1 = Pet("그르르")
# pet1.make_sound()
# pet1.bark()
# pet1.meow()
# pet1.play()


# class Dog():
#     sound = '멍멍'
    

# class Cat():
#     sound = '야옹'
        

# class Pet(Cat, Dog):
#     def __str__(self):
#         super().sound
#         return f"애완동물은 {Pet.sound} 소리를 냅니다."
    
# print(Pet())