#15684
from sys import*
input = stdin.readline

def check():
    for i in range(m):
        s = i
        for j in range(n):
            if a[j][s]: s+=1
            elif s-1 >=0 and a[j][s-1]: s-=1
        if s != i: return 0
    return 1

def solve(idx, cnt, t):
    ans=INF
    if idx == cnt:
        if check(): return cnt
        return ans
    for i in range(t+1, len(can_list)):
        x, y = can_list[i]
        if a[x][y]==0 and a[x][y+1]==0:
            a[x][y]=1
            ans=min(ans, solve(idx+1, cnt, i))
            a[x][y]=0
    return ans

INF = 1e9
m,k,n = map(int,input().split())
a=[[0]*m for _ in range(n)]
can_list=[]
for i in range(k):
    x, y = map(int,input().split())
    a[x-1][y-1] = 1
for i in range(n):
    for j in range(m-1):
        if a[i][j]==0 and a[i][j+1]==0:
            can_list.append((i,j))
ans=INF
for i in range(4):
    ans = solve(0, i, -1)
    if ans != INF:
        print(ans)
        break
if ans==INF: print(-1)
