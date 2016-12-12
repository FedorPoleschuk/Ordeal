n = int(input())

H = dict()
H[1] = [x for x in range(n,0,-1)]
H[2] = []
H[3] = []

def reput(i, k, n):
    if i+k!=4:
        if n == 1:
            disk = H[i].pop()
            H[k].append(disk)
            print("%d %d %d" %(disk,i,k))
        else:
            reput(i, 6-k-i, n-1)
            reput(i,k,1)
            reput(6-k-i,k,n-1)
    else:
        reput(i,2,n)
        reput(2,k,n)

reput(1, 3, n)
