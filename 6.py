def sort(A, B):
    n = 1
    while n < len(A):
        for i in range(len(A) - n):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                B[i], B[i + 1] = B[i + 1], B[i]
                B[i] += 1
                B[i + 1] += 1
        n += 1


def sort2(A, B):
    n = 1
    while n < len(A):
        for i in range(len(A) - n):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                B[i], B[i + 1] = B[i + 1], B[i]
        n += 1


A = list(map(int, input().split()))
B = [0] * len(A)

sort(A, B)

dict = {}
for i in range(len(A)):
    if A[i] not in dict:
        dict[A[i]] = B[i]
    else:
        dict[A[i]] += B[i]


C = list(dict.keys())
D = list(dict.values())

sort2(C,D)

out = []
for i in range(len(C)):
    out.append(str(C[i])+ ':'+ str(D[i]))

print (*out)
