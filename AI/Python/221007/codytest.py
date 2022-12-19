# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여
# F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
# 예를들어
# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 2 이상의 n이 입력되었을 때
# n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.


def sol(n):
    ans = 1
    fir = 0 
    sec = 1
    ans = fir + sec
    for i in range(2, n+1):
        # tmp = sec
        ans =fir + sec
        fir = sec
        sec = ans
    return ans % 123456
 
print(sol(3))


def solution(n):
    answer = 0
    if n == 0:
        answer = 0
    elif n == 1:
        answer = 1
    elif n >= 2:
        for i in range(0, n):
            for j in range (1, n):
                answer =  i + j # f = 1 (0, 1 1)
                if j >= 2:
                    answer += j
    return answer

print(sol(5))

def arrAppend(arr: list): # 변수: list(변수가 리스트만 받음) 변수: lnt(변수가 정수로만 받음)
    arr.append()