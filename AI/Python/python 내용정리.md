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
