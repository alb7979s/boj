from sys import*
from collections import*
input = stdin.readline
def play(f):
    temp = 0
    if f == 0:
        nx, ny = clean, 0
    else: nx, ny = clean+1, 0

    for dx, dy in dd[f]:  #f==0위, f==1 아래
        while 1:
            nx, ny = nx + dx, ny + dy
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                nx -= dx;
                ny -= dy;
                break
            if a[nx][ny] == -1: return
            a[nx][ny], temp = temp, a[nx][ny]

n,m,t = map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
for i in range(n):
    if a[i][0]==-1:
        clean = i       #[i][0], [i+1][0] 공기청전기
        break
dd=[[(0,1),(-1,0),(0,-1),(1,0)],[(0,1),(1,0),(0,-1),(-1,0)]]  #아래쪽 순환
for _ in range(t):
    check=[[0]*m for _ in range(n)]
    for i in range(n):      #확산
        for j in range(m):
            if a[i][j]==-1: continue
            if a[i][j]:
                cnt=0
                for dx, dy in dd[0]:       #위나 아래 아무거나 가능
                    nx, ny = i+dx, j+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>m-1 or a[nx][ny]==-1: continue
                    cnt+=1
                    check[nx][ny]+=(a[i][j]//5)
                check[i][j] += a[i][j] - ((a[i][j]//5)*cnt)
    a=[x[:] for x in check]
    a[clean][0] = -1
    a[clean+1][0] = -1
    #공기청정기 가동
    play(0)
    play(1)
ans=0
for i in range(n):
    for j in range(m):
        if a[i][j]!=-1: ans+=a[i][j]
print(ans)
