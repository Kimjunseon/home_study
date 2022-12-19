from human import Human


class Arm(Human): # 부모는 휴먼
    def __init__(self, side, name) -> None:
        print("팔")
        self.side = side
        super().__init__(name)
        pass