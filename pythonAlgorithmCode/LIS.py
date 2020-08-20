#최장 증가 부분수열
#11053
#v에 계속 넣는데 맨뒤 원소보다 크지 않으면 lower값으로 갱신
from sys import*
input = stdin.readline
def lower(l,r,x):
    while l<=r:
        m = (l+r)//2
        if v[m] >= x:
            r = m - 1
        else:
            l = m + 1
    return l
n=int(input())
arr=list(map(int,input().split()))
v=[arr[0]]
for i in range(1,n):
    if v[-1] < arr[i]:
        v.append(arr[i])
    else:
        v[lower(0,len(v)-1,arr[i])]=arr[i]
print(len(v))
