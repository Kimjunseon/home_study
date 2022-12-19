class Person:
    count = 0 # 비공개속성
    def __init__(self) -> None:
        Person.count += 1 # class Person을 부름
        self.count += 1 # self를 부름


    @classmethod #person이 cls로 들어감
    def printCount(cls): # cls = person
        print(cls.count)
    
    def printCount2(self):
        print(self.count)

        