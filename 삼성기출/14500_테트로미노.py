from sys import*
from collections import*
input = stdin.readline
def dfs(i, j, cnt, res):
    ans=0
    check[i][j]=1
    if cnt == 4:
        check[i][j]=0
        return res
    for dx, dy in dd:
        nx, ny = i+dx, j+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1 or check[nx][ny]: continue
        ans = max(ans, dfs(nx, ny, cnt+1, res+a[i][j]))
    check[i][j]=0
    return ans
def ect(i, j):
    temp=[]
    SUM=a[i][j]
    for dx, dy in dd:
        nx, ny = i+dx, j+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1: continue
        temp.append(a[nx][ny])
    SUM = SUM + sum(temp) - min(temp) if len(temp)==4 else SUM+sum(temp)
    return SUM

n,m = map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
res=0
dd=[(-1,0),(0,1),(1,0),(0,-1)]
check=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        res = max(res, dfs(i,j,0,0), ect(i,j))
print(res)
