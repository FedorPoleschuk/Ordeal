N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))


B = [None]*(N)

for i in range(N):
    if i == 0:
        B[i] = A[i][0]
    elif i == 1:
        B[i] = min(A[0][0] + A[1][0], A[0][1])
    elif i == 2:
        B[i] = min(A[0][0]+ A[1][0] + A[2][0], A[0][1] + A[2][0],A[0][2])
    else:
        B[i] = min(B[i-1] + A[i][0], B[i-2] + A[i-1][1], B[i-3] + A[i-2][2])
print(B[N-1])
