# main
# main 내가 실핼 시킬 것
# java는 무조건 java start
from calc import Calc
from calculator.add import add
from calculator.diff import diff
from person import Person
from user3.age import showAge
from user3.name import showName

def main():
    # showName("park")
    # showAge(21)
    # count = 0
    # count = count + add(count,4)
    # count = diff(count, 10)
    # print(count)
    # showName("park")
    # showAge(21)
    ''' 디버깅 찍어보기 person에 2개 켜서
    p1 = Person()
    p2 = Person()
    p3 = Person()
    print(p1.count)
    print(p2.count)
    print(p3.count)
    '''
    # Calc.add(1,3)
    # Calc.diff(1,3)
    c = Person()
    print(c.count) # 펄슨과 셀프 자체의 합 2
    c.printCount() # cls에 펄슨이 들어간 값 1
    c.printCount2() # 셀프를 불러온 값 2
main()
