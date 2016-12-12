def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    return 0 if get_next.seed == 0 else (get_next.seed**2%100000 + 1)
get_next.seed = int(input())

x = get_next()
max = 0
I = []
n = 0
while x != 0:
    if x > max:
        max = x
        I = [n]
    elif x == max:
        I.append(n)
    x = get_next()
    n += 1

print (*I)