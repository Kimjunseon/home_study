# 정적 -  변화가 없음
from typing import overload


class Calc:
    @staticmethod # @는 어노테이션
    def add(a,b):
        print(a+b)
    # @staticmethod # 스택스을 선언하면 s자리가 self가 됨
    # def diff(s, a, b):
    #     print(a-b)
    #     print("diff 3개")

    @staticmethod
    #@overload
    def diff(s,a):
        print(a+s)
        print("diff 2개")
