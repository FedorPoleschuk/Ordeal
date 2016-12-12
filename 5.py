def sort(A, B):
    n = 1
    while n < len(A):
        for i in range(len(A) - n):
            if A[i] >= A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                B[i], B[i + 1] = B[i + 1], B[i]
        n += 1

A = list(map(int, input().split()))
B = list(map(int, input().split()))

n = 1


sort(A, B)

print(*B)