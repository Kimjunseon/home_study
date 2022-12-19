# 여러가지 모듈
import calendar
import math
import numbers
import random
import re
import webbrowser


# print("3.141592")
# print(math.pi)
# calendar.prmonth(2022, 10)
# # webbrowser.open("https://google.com")
# print(random.random()*11 + 1) # 0 <= answer < 1

# 정규식
# AI 자연어처리 사용
# 비밀번호에서 특수문자, 영어 대문자 포함 등 사용

# 이메일 park@gmail.com 
# reg = re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2, 3})")
# print(reg.match("park@gmail.com"))

#reg = re.compile("[A-z0-9]{2, 3}")
#reg = re.compile("[0-9]{2, 3}") # [A-z0-9] 들어갈 문자 {2, 3} 글자수 2에서 3 (range)
#id = "222"
# print(reg.match(id))
# print(reg.search(id))
# print(type(reg))
# id (222) 내의 {2, 3} 2에서 3 사이의 [0-9] 0에서 9사이 값이 있는가
# 서치에는 발견

# 퀴즈
# 로또 1 ~ 45 중복없이 6자리

# for i in range (0, 5):
#     num = random.random()*45+1
#     print(int(num))



# lotto = []
# for i in range(0, 5):
#     numbers = []
#     while len(numbers) < 6:
#         num = int(random.random()*45+1)
#         tmpNumber = numbers.copy()
#         tmpNumber.append(num)
#         setNumbers = set(tmpNumber.copy())
#         if len(setNumbers) == len(tmpNumber):
#             numbers.append(num)
#         lotto.append(numbers)
#     print(numbers)
# for text in lotto:
#     print(text)

#reg = re.compile("([A-za-z0-9]-[A-za-z0-9]-[A-za-z0-9]{0, 3})")
reg = re.compile("[0-9]{3}-[0-9]{3,4}-[0-9]{4}") # 쉼표 쓰면 안됨
phone_number = "010-5485-4124"
print(reg.match(phone_number))


