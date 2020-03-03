from sys import*
from collections import*
input = stdin.readline
def solve(x, y, dx, dy):
    c=1
    for _ in range(n-1):
        nx, ny = x+dx, y+dy
        diff = a[nx][ny] - a[x][y]
        if abs(diff)>1: return 0    #처음에 여기 절대값 안씌어줘서 틀림
        if diff==1:   #뒤에가 더크면
            if c >= l:  #건설 가능
                c=0
            else:
                return 0
        if diff==-1:
            if c>=0: #앞에 내려오는거 안걸리면
                c = -l
            else:
                return 0
        c+=1
        x, y = nx, ny
    return 1 if c >= 0 else 0
n,l=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
res=0
for i in range(n):
    res += solve(0, i, 1, 0)
    res += solve(i, 0, 0, 1)
print(res)
