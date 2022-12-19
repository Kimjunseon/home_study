# 1. 자연수 뒤집어 배열로 만들기
# 2. 제일 작은 수 제거하기 
# 3. 두 정수 사이의 합
# 4. 정수 제곱근 판별

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.



# 1. 자연수 뒤집어 배열로 만들기
# def solution(n):
#     n = str(n)
#     answer = list(n)
#     answer.reverse()
#     for el in range(0, len(answer)):
#         answer[el] = int(answer[el])
#     return answer
# print(solution(12345))
# map


# 2. 제일 작은 수 제거하기
# def solution2(arr):
#     arr.sort(reverse = True)
#     if len(arr) == 1:
#         arr[0] = -1
#     else:
#         arr.pop()
#     answer = arr
#     return answer
# print(solution2([4,3,5,1]))
# print(solution2([10]))

# def solution2(arr):
#     arr.sort(reverse = True)
#     if len(arr) == 1:
#         arr[0] = -1

#     minNumber = 400000
#     for el in arr:
#         if el  < minNumber:
#             minNumber = el
#     for a in arr:
#         if minNumber != a:
#             arr.append(a)
#     return arr
# print(solution2([4,3,5,1]))
# print(solution2([10]))



# 3. 두 정수사이의 합
# def solution3(a, b):
#     answer = 0
#     if a > b:
#         for el in range(b, a+1):
#             answer = answer + el     
#     elif a == b:
#         answer = a
#     else:
#         for el in range(a, b+1):
#             answer = answer + el

#     return answer

# print(solution3(3,5))

# 4. 정수의 제곱근 판별
# def solution3(n):
#     answer = 0
#     if type((n**(1/2))) == int:
#         n = (n)**(1/2)
#         answer = int((n+1)**2)
#     elif type((n**(1/2))) != int:
#         answer = -1

#     return answer
# print(solution3(4))

# def solution3(n):
#     for i in range(1, n+1):
#         if i**2 == n:      
#             answer = int((n+1)**2)
#             break
#         else:
#             answer = -1
#     return answer
# print(solution3(7))
# print(solution3(8))
# print(solution3(9))
# print(solution3(100))

# def solution4(n):
#     answer = 0
#     for i in range(1, n):
#         if i**2 == n:      
#             answer = i
#             break
#         elif i**2  > n
#             break
#     if answer == 0:
#         return  -1
#     return (answer+1)**2
# print(solution4(7))
# print(solution4(8))
# print(solution4(9))

# def solution(n):
#     answer = 0
#     sum = 0
#     for i in range(1, n+1):
#         for j in range(n, 0, -1):
#             if n == i*j: 
             
#     return answer
# print(solution(3))



 