# 2부터 20까지 짝수의 합

sum = 0
for i in range(2, 21, 2):
    sum = sum + i
print(sum)

while i <= 20:
    if 1%2 == 0:
        sum += 1
        i += 1
print(sum)

# 