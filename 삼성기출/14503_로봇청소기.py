from sys import*
from collections import*
input = stdin.readline
def solve():
    while q:
        f = 1
        x, y, d = q.popleft()
        visit[x][y]=1
        for i in range(4):
            d = (d + 3) % 4
            dx, dy = dd[d]
            nx, ny = x + dx, y + dy
            if a[nx][ny] or visit[nx][ny]: continue
            q.append((nx, ny, d))
            f = 0
            break
        if f:  # 4방향 청소 못했으면
            nx, ny = x - dx, y - dy
            if a[nx][ny]: #끝
                res=0
                for i in range(n):
                    res+=visit[i].count(1)
                return res
            q.append((nx, ny, d))        #방향 유지해줘야 하는데 (d+2)%4 해줬다가 무한루프 돌았었음
dd=[(-1,0),(0,1),(1,0),(0,-1)]  #URDL
n,m=map(int,input().split())
r,c,d = map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
q=deque()
q.append((r,c,d))
visit=[[0]*m for _ in range(n)]
print(solve())
