# 업데이트 및 클래스
# 계산기 만들기
# def add(a, b):
#     return a+b

# def diff(a, b):
#     return a-b
# i = 0
# i = add(i, 10)
# i = diff(i, 5)
# print(i)

# class
# class Calculator:
#     def __init__(self) -> None: # init(initial) 초기값설정, self 자기자신
#         self.result = 0
            
#     def add(self, b):
#         self.result += b

#     def diff(self, b):
#         self.result -= b

# from cal import Calculator

# call = Calculator()
# call.add(10)
# call.diff(5)
# print(call.result)

# cal2 = Calculator()
# cal2.add(7)
# cal2.diff(8)
# print(cal2.result)

# class 내 super는 부모

from locale import RADIXCHAR
from os import scandir
from cat import Cat
from dog import Dog
from user import User
from animaltype import Animal
from human import Human
from arm import Arm
from leg import Leg


user1 = User("bit", "1234")
user1.printUser()
user1.change_id("tib")
user1.printUser()

l = Leg("left", "park")
a = Arm("right", "kim")
l.setName("kim")
print(l.name)

an = Animal()
print(an.name)
an.__setattr__("name", "?") # "name" 을 ? 로 변경
print(an.name)
print(an.__dict__)


cat = Cat()
cat.printSound()
print(cat.name)

dog = Dog()
dog.printSound()
print(dog.name)
print(dog.master)
print(dog.__dict__)
# {'name': '멍멍', 'master': True} = Dog < = 객체
# human = {name age gender...} [객체]
# 절차 지향

# 클래스느 하나의 물체를 만들기 위해 사용
# 상속은 공통코드를 줄이기위해서
