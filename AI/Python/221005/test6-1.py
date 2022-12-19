# 221005 수업
# 구구단
num = 2
for i in range (2,10):
    for j in range (1,10):
        print(f"{i} * {j} = {j * i}")

# 별 그리기
# *
# **
# ***
# ****
# *****
text = "*"
for i in range(2,7):
    st = ""
    for j in range(1, i):
        st = text * j
    print(st)



# 2 부터 30 까지 소수 리스트 뽑아내기
#소수는 1보다 크고 그 숫자 자신 보다 작은 수 2개를 곱해서 만들 수 없는 수다.
list = []
for el in range(2, 31):
    for el2 in range (2, el+1):
        if el % el2 == 0:
            break
    if el == el2:
        list.append(el)
print(list)

'''
answer = []
for i in range(2, 31):
    isPrimary = True
    for j in range(2, i):
        if i % j == 0:
            isPrimary = False
            break
    if isPrimary:
        answer.append(i)
print(answer)
'''
