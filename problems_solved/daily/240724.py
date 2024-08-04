# # 아래 클래스를 수정하시오.
# class StringRepeater:
#     @staticmethod
#     def repeat_string(num, string):
#         for i in range(num):
#             print(string)
#
#
# repeater1 = StringRepeater()
# repeater1.repeat_string(3, "Hello")

# class Person:
#     number_of_people = 0
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.number_of_people += 1
#
#     def introduce(self):
#         print(f'제 이름은 {self.name} 이고, 저는 {self.age} 살 입니다.')
#
#
# person1 = Person("Alice", 25)
# person1.introduce()
# print(Person.number_of_people)

# 아래에 코드를 작성하시오.
# my_list = [1, 2, 3]
# my_dict = {'A': 1, 'B': 2, 'C': 3}
#
# print(dir(my_list))
# print(dir(my_dict))
# help(my_list)
# help(my_dict)

# class Myth:
#     type_of_myth = 0
#
#     def __init__(self, name):
#         self.name = name
#         Myth.type_of_myth += 1     # self. 는 카운트가 되지 않는다
#
#     @staticmethod
#     def description():
#         print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')
#
#
# myth1 = Myth('dangun')
# myth2 = Myth('greek & rome')
#
# print(myth1.name)
# print(myth2.name)
# print(Myth.type_of_myth)
# Myth.description()

# class Car:
#     wheels = 4
#
#     def __init__(self, engine, driving_system, sound):
#         self.engine = engine
#         self.driving_system = driving_system
#         self.sound = sound
#
#     def drive(self):
#         print(self.sound)
#         return self.engine
#
#     def introduce(self):
#         print(f'제 차의 엔진은 {self.engine} 방식이고, {self.driving_system} (으)로 동작합니다.')
#
#     @classmethod
#     def increase_wheels(cls):
#         cls.wheels += 1
#         print('법이 개정되어 모든 자동차의 필요 바퀴 수가 1증가하였습니다.')
#
#     @staticmethod
#     def description():
#         print('자동차(自動車, 영어: car, automobile)는 엔진에서 만든 동력을 바퀴에 전달하여 지상에서 승객이나 화물을 운반하는 교통 수단이다.')
#
#
# car1 = Car('gasoline', '후륜구동', '부릉부릉')
# car2 = Car('diesel', '전륜구동', '달달달달')
# car3 = Car('hybrid', '4wd', '슈웅')
#
# car1.drive()
# print(car2.drive())
#
# print('===')
# car1.introduce()
# car3.introduce()
#
# print('===')
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.increase_wheels()
# print(f'이 세상의 자동차는 {Car.wheels}개의 바퀴를 가집니다.')
# Car.description()

# main.py
# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def print_info(self):
        print(f'Width: {self.width}\nHeight: {self.height}\n'
              f'Area: {self.calculate_area()}\nPerimeter: {self.calculate_perimeter()}')

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)


