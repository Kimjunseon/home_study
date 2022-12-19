# 함수
# define 정의

# 파이썬 절차 지항
# 자바 OPP 객체 지향

# isPrimary = True cammel case
# is_Primary_key = True snake case

from tkinter import E


def sum(a, b): # a, b는 매개변수
    return a + b

print(sum(1,2)) # (sum(1,2)) => 1, 2는 인수

# def sum1():
#     return 2+2
# print(sum1())

def sum1(*args): # * 이 붙으면 여러 인자를 부여 가능, tuple 생성 (* 한개)
    pppp = 0
    for arg in args:
        pppp += arg
    return pppp

print(sum1(1,1,1,1,1,1))    
print(sum1(1,2,3,4,5))

def printFunc(**kwargs): # dict 생성 (* 두개)
    print(kwargs)
printFunc(a = 1, b =1, c = 1)

def makeHuman(name, age):
    return {"name" : name , "age" : age}

human1 = makeHuman("kim", 30)
human2 = makeHuman("park", 20)
human3 = makeHuman("lee", 35)
print(human1)


# 함수를 사용한 소수 판결
def isPrimaryNumber(num):
    isPrimary = True
    for j in range(2, num):
        if num % j == 0:
            isPrimary = False
            break
    if isPrimary:
        return f"{num} 은 소수입니다"
    else:
        return f"{num} 은 소수가 아닙니다"

print(isPrimaryNumber(2))

# 함수를 사용한 소수 판결 (다수) #tuple 구조이므로 for을 사용, for 구문은 반복이므로 return이 에러가 남
def isPrimaryNumbers(*nums):
    for num in nums:
        isPrimary = True
        for j in range(2, num):
            if num % j == 0:
                isPrimary = False
                break
        if isPrimary:
            print(f"{num} 은 소수입니다")
        else:
            print(f"{num} 은 소수가 아닙니다")

isPrimaryNumbers(2,3,4,5,6,7)
print(isPrimaryNumbers(2,3,4,5,6,7)) # None 뜨는 이유는 리턴값이 없음

# 지역변수 전역변수
name = "park" # 전역변수

def setName1(name):
    name = name # 지역변수
    print(name)
    name = name
    print(name)
setName1("kim")
print(name)

