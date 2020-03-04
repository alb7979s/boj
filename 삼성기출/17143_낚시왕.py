from sys import*
from collections import*
input = stdin.readline
def move():
    temp=[]
    check=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j]:
                speed, d, size = a[i][j]
                a[i][j]=0
                dx, dy = dd[d]
                nx, ny = i, j
                for k in range(speed):
                    nx, ny = nx+dx, ny+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>m-1:
                        nx, ny = nx-2*dx, ny-2*dy
                        d = searchD(d)
                        dx, dy = dd[d]
                if not check[nx][ny]:       #첫 방문
                    temp.append((nx, ny))
                    check[nx][ny]=(speed, d, size)
                else:   #있으면
                    if check[nx][ny][-1] < size:    #사이즈 비교
                        check[nx][ny] = (speed, d, size)
    for x, y in temp:
        a[x][y] = check[x][y]
def searchD(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    else: return 2
n,m,k=map(int,input().split())
a=[[0]*m for _ in range(n)]
dd=[(-1,0),(1,0),(0,1),(0,-1)]
for i in range(k):
    x,y,speed,d,size=map(int,input().split())
    a[x-1][y-1] = (speed, d-1, size)
res=0
for i in range(m):
    for j in range(n):
        if a[j][i]:
            res+=a[j][i][-1]
            a[j][i]=0
            break
    move()
print(res)
