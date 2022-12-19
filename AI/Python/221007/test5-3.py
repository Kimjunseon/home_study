# 람다는 3.6 이상
# 예제) list1의 요소를 *2해서 찍기
#list1 = [1,2,3,4,5,6,2,3,5,1]
#list2 = []

#for el in list1:
#    list2.append(el*2)
#print(list2)

# map은 새로운 리스트를 만든다. (반환)
#list4 = list(map(lambda x : x*2 ,list1))
#print(list4)

#from functools import reduce

# list1 = [1,2,3,4,5,6,2,3,5,1]
# sum = 0

# for el in list1:
#     sum += el
# print(sum)

# sum2 = reduce(map(lambda x,y : x+y , list1))
# print(s)

# list0  = []
# list1 = [1,2,3,4,5,6,2,3,5,1]

# for el in list1:
#     if el >= 4:
#         list0.append(el)
# print(list0)

# list01 = list(filter(lambda x : x >=4 , list1))
# list01

# x = {"company" : "비트", "isPartTime" : "비정규직"}


# if x.get("company") == "카카오":
#     print("대기업 직권이시네요")

# elif x.get("company") == "네이버":
#     print("대기업 직권이시네요")

# else:
#     print("중견기업 직원이시네요")


# Q. phone = {"name" : "갤럭시", "version" : "플립"}
# phone이 애플이면 와우
# 갤럭시면 version을 보고 플립이면 접히네요
# 아니면 좋네요

from bdb import Breakpoint
from mailbox import ExternalClashError


phone = {"name" : "갤럭시", "version" : "노트"}

if phone.get("name") == "갤럭시":
    if phone.get("version") == "플립":
        print("접히네요")

elif phone.get("name") == "애플":
    print("와우")
else:
    print("좋네요")


# break continue
# list1 = [9,4,2,1,6,7,5,4,3,7]
# 만약에 홀수면 2배 짝수면 그냥
# 합이 20이 넘으면 끝

# list1 = [9,4,2,1,6,7,5,4,3,7]
# list2 = []
# sum = 0

# for el in list1:
#     if sum <= 20:
#         if list1[el] % 2 == 1:
#             list2.append(el*2)
#             print(sum)

#         elif list1[el] % 2 == 0:
#             list2.append(el)
            
    
#     elif sum > 20:
#         break


# print(list2)


list1 = ["안", "녕", "하", "세", "요"]
index = 0
hi = ""
while index < len(list1):
    hi += list1[index]
    index += 1
print(hi)

for el in list1:
    hi = hi + el
print(hi)


st = "안녕하세요"
print(st[0])
for elment in st:
    print(elment)
    