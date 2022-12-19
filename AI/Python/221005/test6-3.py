# 코딩 테스트 (1. 백준(31%) 2. 프로그래머스(30%))

# 문제 설명
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

# def solution(num):
#     if num % 2 == 1:
#         answer = 'ODD'
#     elif num % 2 == 0:
#         answer = 'EVEN'
#     return answer

# print(solution(3))
# print(solution(4))
# print(solution(5))

# a = input("입력하세요")
# print(a)

# 형 변환, 오류
# def sum(a,b):
#     try:
#         if type(a) == int and type(b) == int:
#             return a + b
#         else :
#             return int(a) + int(b)
#     except:
#         return f"{a}와 {b} 중 숫자가 아닌게 있습니다."

# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))

# 3,6,9 게임
# 들어온 숫자에 3,6,9 면 c
# 계속 지속이며 다른 값 입력 시 실패

from multiprocessing.connection import answer_challenge
# def game(cur, mylnput):
#     answer = str(cur + 1)
#     for c in str(cur + 1):
#         if c == "3" or c == "6" or c == "9":
#             answer = "c"
#     if myInput == answer:
#         print("Pass")
#         return True
#     else:
#         print("Game over")
#         return False

#     # if myInput != str(i+1):
#     #     print("졌습니다")
#     #     break
# i = 0
# while True:
#     i += 1
#     myInput = input(f"현재값 [{i}]")
#     isWin = game(i, myInput)
#     if(not isWin):
#         break

    
    # if a % 3 == 0:
    #     a = input(f"369369 [현재 {i}] ")
    #     i += 1
    #     if a != c:
    #         print("졌습니다")
        

    # elif a % 3 == 1:
    #     a = input(f"369369 [현재 {i}] ")
    #     i += 1
    #     if a == c:
    #         print("졌습니다")

# 코딩테스트
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
# 제한조건 phone_number는 길이 4 이상, 20이하인 문자열입니다.
# input으로 번호 받아서 010-0000-1111 받고 출력은 ***-***-1111
# len13
# pn = input("전화번호 :")
# def solution(phone_number):
#     for i in range(0, len(phone_number)):
#         if i > 3:
#             answer = phone_number.replace(phone_number[i], "*")
#         elif i == 3 :
#             answer = phone_number.replace(phone_number[i], "-")
#         elif i < 7 and i > 3:
#             answer = phone_number.replace(phone_number[i], "*")
#         elif i == 7:
#             answer = phone_number.replace(phone_number[i], "-")
#         elif i > 7:
#             continue
#     return answer
# solution(pn)
# print(solution(pn))

# def solution(phone_number):
#     answer = ''
#     for i in range(0, len(phone_number)):
#         if i < len(phone_number) - 4:
#             if phone_number[i] == "-":
#                 answer += "*"
#             else:
#                 answer += "*"
#         else:
#             answer += phone_number[i]
#     return answer
# phone_number = input("전화번호")
# print(solution(phone_number))

# 파일 입출력
# 상대경로
# . 현재위치 c/test
# .. c 전 위치

# 절대경로 C:\test 방식

# f = open("./test.txt", 'w')
# f.write("hi\n")
# f.write("\n")
# f.write("\n")
# f.write("\too")
# f.close()

# f = open("./test.txt", 'r')
# lines = f.readlines() # 전 라인 읽기
# for line in lines:
#     print(line)
# f.close()
