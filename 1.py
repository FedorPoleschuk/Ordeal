x = int(input())

i = 0
while x > 33:
    if x % 36 == 33:
        i += 1
    x = x // 36
if x == 33:
    i += 1
print(i)
