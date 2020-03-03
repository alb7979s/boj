from sys import*
from collections import*
input = stdin.readline
n,l,r = map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
res = 0; time=0
dd=[(-1,0),(0,1),(1,0),(0,-1)]
while 1:
    f = 0
    check=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                q=deque(); SUM=a[i][j]; cnt=1; temp=[]
                q.append((i, j))
                temp.append((i, j))
                check[i][j]=1
                while q:
                    x, y = q.popleft()
                    for dx, dy in dd:
                        nx, ny = x+dx, y+dy
                        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or check[nx][ny]: continue
                        if l <= abs(a[nx][ny]-a[x][y]) <= r:
                            cnt += 1
                            temp.append((nx, ny))
                            SUM += a[nx][ny]
                            q.append((nx, ny))
                            check[nx][ny]=1
                if cnt >= 2:
                    f=1
                    for x, y in temp:
                        a[x][y] = SUM//cnt
    if not f: break
    time+=1
print(time)
