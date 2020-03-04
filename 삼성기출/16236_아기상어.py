#가장 가까운곳 위, 왼쪽 부터 가는거 bfs()로 가까운곳+dd방향설정으로
#될 줄 알았는데 예외 있음, 아예 거리 + x,y좌표도 정렬해서 찾아줘야함 그래서 heapq씀

from heapq import*
from sys import*
input = stdin.readline

n=int(input())
a=[]; pq=[]
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(n):
        if a[i][j] == 9:
            heappush(pq,(0,i,j))
            a[i][j]=0
dd=[(-1,0),(0,1),(1,0),(0,-1)]
size, res, eat = 2, 0, 0
check=[[0]*n for _ in range(n)]
while pq:
    d, x, y = heappop(pq)
    check[x][y]=1
    if 0< a[x][y] < size:  #먹음
        pq=[]
        heappush(pq, (d,x,y))
        eat += 1
        res += d
        a[x][y]=0
        if eat == size:
            eat = 0
            size+=1
        d=0
        check=[[0]*n for _ in range(n)]
    for dx, dy in dd:
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or check[nx][ny] or a[nx][ny] > size: continue
        heappush(pq, (d+1, nx, ny))
        check[nx][ny]=1
print(res)


