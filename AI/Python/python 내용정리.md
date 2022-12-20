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


