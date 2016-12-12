x = int(input())
i = 0
while x > 16:
    if x % 17 == 16:
        i += 1
    x = x // 17
if x == 16:
    i += 1
print(i)