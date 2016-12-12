A = list(map(int, input().split()))
n = A[0]
k = A[1]

B = []
s = ''
def dist(s ,n, k):
    if n == 1:
        s += str(k)
        B.append(s)
    else:
        if n == k:
            dist(s + '1', n-1, k-1)
        elif k == 0:
            dist(s + '0', n-1, k)
        else:
            dist(s + '0', n-1, k)
            dist(s + '1', n-1, k-1)


dist('', n, k)

for i in B:
    print(i)
print()
