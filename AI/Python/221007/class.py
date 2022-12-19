# 마린 : 공격 유닛, 군인. 총을 쓴다

# class Unit:
#     def __init__(self, name, hp, damage) -> None:
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f"{name} 유닛이 생성 되었습니다.")
#         print(f"체력 {hp}, 공격력 {damage} 유닛이 생성 되었습니다.")

# mar1 = Unit("마린", 40, 5)
# mar2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# raith = Unit("레이스", 80, 5)
# print(f"유닛이름 : {raith.name}, 공격력 : {raith.damage}")

#파이썬에서는 클래스 외부에서 변수를 생성할수있다?
raith2 = Unit("레이스2", 80, 5)
raith2.clock = True
if raith2.clock == True:
    print(f"{raith2.name}는 클로킹상태")

# 매서드
# class Attack:
#     def __init__(self, name, damage) -> None:
#         self.name = name
#         self.hp = hp
#         self.damamge = damage
#     def attack(self, loca)
#         print(f"{raith2.name} : {damage} 방향으로 적군을 공격합니다. 공격력 [{damage}]")