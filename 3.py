def get_next():
    get_next.seed = (get_next.seed*513 + 1)%2**18
    if get_next.seed == 0:
        return 0
    else:
        return (get_next.seed**2 + 3*get_next.seed)%999 + 1
get_next.seed = int(input())

x = get_next()
seq = {}
while x != 0:
    if x not in seq:
        seq[x] = 1
    else:
        seq[x] += 1
    x = get_next()

max = 0
A = []
for key in seq:
    if seq[key] > max:
        max = seq[key]
        A = [key]
    elif seq[key] == max:
        A.append(key)

A = sorted(A)

print(*A)