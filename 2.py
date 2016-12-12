str = list(map(int, input().split()))
A = []

while str != [0,0]:
    A.append(str)
    str = list(map(int, input().split()))

n = 0

for pair in A:
    if (pair[0] % 3 == 0 and pair[1] % 2 == 0 and pair[1] % 3 != 0) or (pair[1] % 3 == 0 and pair[0] % 2 == 0 and pair[0] % 3 != 0) or (pair[0] % 9 == 0 and pair[1] % 9 == 0):
        n += 1

print (n)