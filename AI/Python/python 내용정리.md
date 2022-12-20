# List Comprehension

- 반복문 처리 : for문과 같은 동작을 함

## for문을 사용한 반복

```
for i in range(10):
	result.append(i);

print(result)
print()
```

## List Comprehension문을 사용한 반복

```
result2 = [i for i in range(10)]
print(result2)
```

## if문을 사용한 짝수처리

- for
```
result = []

for i in range(10):
    if i % 2 == 0:
        result.append(i)

print(result)
print()
```
- List Comprehensio

```
result2 = [i for i in range(10) if i % 2 == 0]
print(result2)
```

## else문을 사용한 List Comprehension


- for
```
result = []

for i in range(10):
    if i % 2 == 0:
        result.append(i)
    else:
        result.append(99)
        
print(result)
print()
```

- List Comprehension
```
result2 = [i if i % 2 == 0 else 99 for i in range(10)]
print(result2)
```
else를 사용할 땐 if문을 앞으로 for문을 뒤로 보낸다
```
i if (조건) else (조건) for (조건)
```

## 이중 for문에서 List Comprehension 사용

- for
```
result = []
case1 =  ['A', 'B', 'C']
case2 =  ['A', 'B', 'C']

for i in case1:
    for j in case2:
        result.append(i + j)
print(result)
```
- List Comprehension
```
result2  = [i + j for i in case1 for j in case2]
print(result2)

if i !=j 조건을 추가하면 중복이 제거 됨
```
# Numpy
## Numpy는...
- 과학 계산을 위한 라이브러리
- 행렬/배열 처리 및 연산
- 난수생성
     
- numpy를 import 하는 법
```
import numpy as np
```
- 데이터 타입 알아보기
```
a1 = np.array([0, 1, 2, 3, 4, 5])

type(a1)	a1의 타입
a1.dtype	a1의 데이터 타입
```



