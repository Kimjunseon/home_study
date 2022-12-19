# # tmp = {"name" : "lee" , "age" : 30}
# # tmp2 = tmp.copy()

# # print(tmp)
# # print(tmp2)
# # print("")

# # tmp["name"] = "kim"
# # tmp["age"] = 15
# # print(tmp)
# # print(tmp2)
# # print("")

# # list = [tmp]
# # list.append(3)
# # print(tmp)
# # print(list)
# # print(tmp2)

# # list = [1,2,3]
# # list2 = list.copy()
# # list.append(4)

# # print(list)
# # print(list2)

# #람다사용
# list2 = [1,2,3,4,5,6,7]
# #변수의 합
# a = (lambda x,y : x+y)(10, 20)
# b = (lambda x,y,z : x+y+z)(10, 20, 30)
# c = (lambda x,y,z : x+y*z)(10, 20, 5)
# print(a)
# print(b)
# print(c)

# #map 사용 [함수와 리스트를 인자로 받음]
# d = list(map(lambda x : x, range(5))) # map 함수로 인해 0,1,2,3,4 생성 list로 [0,1,2,3,4]
# d = list(map(lambda x : x, list2)) #list2 값도 받을 수 있다.
# names = ["kim", "lee", "park"]
# namelist = list(map(lambda x : {"id":"id", "password":"password", "name" : x}, names))
# print(namelist)
# print(d)

# #reduce [변수 인자들을 곱]
# from functools import reduce
# from logging.config import valid_ident
# from mailbox import _PartialFile
# import re #reduce를 사용하기 위한 함수
# e = reduce(lambda x,y : x+y, range(5)) # 0,1,2,3,4 합
# f = reduce(lambda x,y : x*y, range(5))
# print(e)
# print(f)

# #filter [조건 반환]
# g = list(filter(lambda x : x > 3, list2))
# print(g)

# test = [1,2,3]
# test2 = test.copy()
# test3 = list(map(lambda x : x, test))

# print(test)
# print(test2)
# print(test3)
# print("")

# test.append(4)
# print(test)
# print(test2)
# print(test3)

# print(id(test2))
# print(id(test3))

# 복습
# '''
# Q1. 2부터 20까지 짝수합
# Q2. 김씨 박씨 돈의 합
# Q3. 리스트 내의 홀짝 구분
# Q4. 리스트 내 홀2배 짝 그대로 15넘으면 break
# '''
# # Q1
# sum = 0
# for i in range(2, 21, 2):
#     sum = sum + i 
# print(sum)

# # Q2
# q1 = {"name" : "kim" , "money" : 5000}
# q2 = {"name" : "park" , "money" : 3000}
# print("%s과 %s의 돈의 합은 %d원 입니다,"%(q1.get("name"), q2.get("name"), q1.get("money") + q2.get("money")))

# # Q3
# q_3 = [1,2,45,12,124,32,333,1267,23,2,74]

# for i in range(0, len(q_3)):
#     if q_3[i] % 2 == 0:
#         print(f"{q_3[i]}는 짝입니다.")
#     else:
#         print(f"{q_3[i]}는 홀입니다.")


# for el in q_3:
#     if  el % 2 == 0:
#         print(f"{el}는 짝입니다.")
#     elif el % 2 == 1:
#         print(f"{el}는 홀입니다.")


# # Q4
# q4 = [4, 5, 1, 7, 2, 4, 5, 9, 3]
# q4_1 = []
# sum_q4 = 0

# for i in q4:
#     sum_q4 = sum_q4 + i

#     if i % 2 == 1:
#         q4_1.append(2*i)

#     elif i % 2 == 0:
#         q4_1.append(i)
#         if sum_q4 > 15:
#             break
# print(q4_1)
# print("4, 10, 2, 14, 2")

# q4_i = 0
# sum2 = 0
# qlist = []

# while q4_i < len(q4):
#     sum2 = sum2 + q4[q4_i]

#     if q4[q4_i] % 2 == 1:
#         qlist.append(2*q4[q4_i])
#         q4_i += 1

#     elif q4[q4_i] % 2 == 0:
#         qlist.append(q4[q4_i])
#         q4_i += 1
#         if sum2 > 15:
#             break

# print(qlist)


# # 소수점 표시
# print("소수점 표기 %f"%(10/3)) # %d는 정수 %f는 실수
# print("소수점 표기 %.3f"%(10/3)) # %.nf 소수점 n자리까지 표기 (단, n은 정수)
# print("소수점 표기 %   f"%(10/3)) # f앞에 0이상 숫자 또는 공백은 출력시 해당 크기만큼 띄어쓰기

# # 문자열 나누기, 바꾸기
# char = "hello"
# print(char.split("e")) # 문자를 기준으로 나눔
# print(char.replace("e", "i")) # 문자 바꾸기

# # 리스트 내 중복 숫자 제거, 맨 뒤 제거, 값 끼어넣기
# # 중복제거
# testlist = [2,2,3,4,5,7,7]
# testlist.remove(7) # 리스트 내 중복 숫자를 한번만 제거 
# print(testlist)

# # 맨 뒤 제거
# testlist2 = [2,2,3,4,5,7,7]
# testlist2.pop(4) # pop(4)번지 숫자 제거
# print(testlist2)

# # 값 끼어넣기
# testlist3 = [2,2,3,4,5,7,7]
# testlist3.insert(1, 9) #(n번째 자리 오른쪽, 문자추가)
# print(testlist3)

# # Set 함수의 합, 차, 교집합

# pratice_set = {1,2,3}
# pratice_set2 = {2,3,4}

# print(pratice_set | pratice_set2) # 합집합
# print(pratice_set - pratice_set2) # 차집합 (A - B)
# print(pratice_set & pratice_set2) # 교집합

# # 포맷
# py = 3
# py2 = 5
# print(f"{py} + {py2} = {py + py2}")
# print("%d + %d = %d"%(py, py2 , py + py2))
# print("{0} + {1} = {2}".format(py, py2, py + py2))

# # 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")
        
# # 별 그리기
# star ="*"
# for i in range(2, 7):
#     eli = ""
#     for j in range(1, i):
#         eli = star * j
#     print(eli)

# # 2부터 50까지의 소수 뽑기
# prime = []
# for pi in range(2, 51):
#     for pj in range (2, pi+1):
#         if pi % pj == 0:
#             break
#     if pi == pj:
#         prime.append(pi)
# print(prime)

# # 함수와 매개변수
# def sum(a1, b1):
#     return a1 + b1

# print(sum(3, 4))

# ki = "hello"
# print(ki[1])

# # 매개변수 튜플, 딕셔너리 확인
# # 튜플
# def nums(*args):
#     pln = 0
#     for i in args:
#         pln += i
#     return pln
# print(nums(2, 2, 2))
# print(nums(1, 2, 3))

# # 딕셔너리
# def pradcit(name, age):
#     return {"name" : name, "age" : age}

# h1 = pradcit("ki", 30)
# print(h1)



# def pra(*args):
#     ppp = 0
#     for arg in args:
#         ppp += arg
#     return ppp
# print(pra(1,1,1))
# print(pra(1,2,3))

# # 코딩테스트
# # 홀 짝 반환
# # 369 게임
# # 번호가리기
# # 파일입출력
# # 경로
# # 파일 생성 파이썬 및 텍스트

# 객체지향, Class 자바는 Method C++ member
class Car:
    # field (필드) 영역
    color = ""
    speed = 0

    # method 영역 (클래스 내 함수는 메서드라 함)
    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car()
myCar1.color = "red"
myCar2 = Car()
myCar2.color = "green"
myCar3 = Car()
myCar3.color = "black"