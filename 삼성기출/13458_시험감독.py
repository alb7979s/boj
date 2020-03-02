n=int(input())
a=list(map(int,input().split()))
b, c = map(int,input().split())
res = 0
for i in range(n):
    a[i] -= b; res += 1 #총감
    if a[i] > 0:
        if a[i] % c ==0: res += a[i]//c
        else:
            res += a[i]//c + 1
print(res)
