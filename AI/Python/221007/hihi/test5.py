# 제어문 22년 10월 4일 (화)

'''
[복습]
1. 80이 짝수인가?
Q.
print(f"80이 짝수인가 {80%2==0}")

2. 리스트 [2, 1, 5, 6, 40, 50, 2, 5, 32] 와 리스트  [4, 6, 2, 3, 9, 10, 2, 3, 42, 5, 4, 63] 의 교집합 중 최댓값 출력
Q.
list = [2, 1, 5, 6, 40, 50, 2, 5, 32]
list2 = [4, 6, 2, 3, 9, 10, 2, 3, 42, 5, 4, 63]
set(list) & set(list2)
setmax = set(list) & set(list2)
max(setmax)
--------------------------------------------------------------------------------------------------------------------
union = list(set(list) & set(list2))
union.sort()
print(union[len(union) - 1]

# print(f"a>b {a>b} = True 크다 False 작다")
'''

# 조건에 따라 출력
a = 1155
b = 110
c = [1, 2, 3, 4, 5]

if a>b: # a가 b 보다 크면
    print(f"a > b 크다")
    
elif a<b: # a가 b 보다 작으면
    print(f"a > b 작다")
    
else: # a와 b가 같으면
    print(f"a = b 같다")
    

if a>b: # a가 b 보다 크면
    str1 = "크다"
elif a<b: # a가 b 보다 작으면
    str1 = "작다"
else: # a와 b가 같으면
    str1 = "같다"

# if문 2개이상 연속은 else 판정이 아님, len(c) = 4
if len(c) >= 3:
    print(c[0])

if len(c) > 2:
    print(c[0])

str1

