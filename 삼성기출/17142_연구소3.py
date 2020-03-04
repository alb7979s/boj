from sys import*
from collections import*
input = stdin.readline
def solve(pos, cnt):
    ans=INF
    if cnt > m: return ans
    if pos == len(virus_list):
        if cnt == m:
            ans = min(ans, play())
        return ans
    virus.append((virus_list[pos]))
    ans = min(ans, solve(pos+1, cnt+1))
    virus.pop()
    ans = min(ans, solve(pos+1, cnt))
    return ans
def play():
    q=deque()
    check=[[0]*n for _ in range(n)]
    cnt=0
    for x, y in virus:
        q.append((x,y,0))
        check[x][y]=1
    while q:
        x,y,t = q.popleft()
        for dx, dy in dd:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or check[nx][ny] or a[nx][ny]==1:continue
            q.append((nx,ny,t+1))
            check[nx][ny]=1
            if not a[nx][ny]:
                cnt+=1
                if zero == cnt: return t+1
    return INF

dd=[(-1,0),(0,1),(1,0),(0,-1)]
INF=1e9
n,m=map(int,input().split())
a, virus, virus_list = [], [], []
zero=0
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(n):
        if a[i][j]==2:
            virus_list.append((i,j))
        elif a[i][j]==0:
            zero+=1
res=solve(0,0) if zero !=0 else 0
print(res if res!=INF else -1 )
