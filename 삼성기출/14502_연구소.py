from sys import*
from collections import*
input = stdin.readline

def bfs():
    q=deque()
    visit=[[0]*m for _ in range(n)]
    for x, y in virus:
        q.append((x, y))
        visit[x][y]=1
    cnt=0
    while q:
        x, y = q.popleft()
        for dx, dy in dd:
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or a[nx][ny]!=0: continue
            visit[nx][ny]=1
            cnt += 1
            q.append((nx, ny))
    return zero - cnt

n,m = map(int,input().split())
a=[]; zero=-3   #벽 세개 놓을꺼라
virus=[]; res=0
dd=[(-1,0), (0,1), (1,0), (0,-1)]
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        if a[i][j] == 2:
            virus.append((i,j))
        elif a[i][j]==0:
            zero += 1
for ix in range(n):
    for iy in range(m):
        for jx in range(n):
            for jy in range(m):
                if ix==jx and iy==jy: continue
                for kx in range(n):
                    for ky in range(m):
                        if (kx==jx and ky==jy) or (kx==ix and ky==ix): continue
                        if not (a[ix][iy] or a[jx][jy] or a[kx][ky]):       #전부 0이면
                            a[ix][iy], a[jx][jy], a[kx][ky] = 1, 1, 1
                            res = max(res, bfs())
                            a[ix][iy], a[jx][jy], a[kx][ky] = 0, 0, 0
print(res)
