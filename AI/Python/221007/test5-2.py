# list = [1,2,3,4,5,6,2,3,5,1]
# 짝, 홀 구별

list = [1,2,3,4,5,6,2,3,5,1]

for i in range (0, len(list)):
    if list[i] % 2 == 0:
        print(f"{list[i]} 는 짝수입니다.")
    else:
        print(f"{list[i]} 는 홀수입니다.")

'''
[for 구문]
list1 = [1,2,3,4,5,6,2,3,5,1]
for el in list1:
    if el % 2 == 0:
        print{f"{el}" 은 짝수 입니다.}
    elif el % 2 == 1:
        print{f"{el}" 은 홀수 입니다.}
    else:
        print("0 입니다.")
#[while 구문]
list1 = [1,2,3,4,5,6,2,3,5,1]
while i < len(list1):
    if list1[i] % 2 == 0:
        print(f"{list1[i]} 은 짝수 입니다.")
    elif list1[i] % 2 == 1:
        print(f"{list1[i]} 은 홀수 입니다.")
    else:
        print("0 입니다.")
    i += 1
'''

