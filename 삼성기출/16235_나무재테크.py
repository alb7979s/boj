from sys import*
from collections import*
input= stdin.readline
dd=[(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
def solve():
    global  cnt
    for i in range(n):
        for j in range(n):  #봄,여름
            die = []
            for k in range(len(q[i][j])):
                x = q[i][j].popleft()
                if a[i][j] < x: #양분 적으면
                    die.append(x)
                else:           #양분 충분
                    a[i][j]-=x
                    q[i][j].append(x+1)
            for x in die:
                a[i][j]+=(x//2)
                cnt-=1

    for i in range(n):      #가을, 겨울
        for j in range(n):
            for k in range(len(q[i][j])):
                if q[i][j][k] % 5 == 0: #5의 배수이면
                    for dx, dy in dd:
                        nx, ny = i+dx, j+dy
                        if nx<0 or ny<0 or nx>n-1 or ny>n-1: continue
                        q[nx][ny].appendleft(1)
                        cnt+=1
            a[i][j]+=add[i][j]

cnt=0
n,m,k=map(int,input().split())
add=[]  #양분추가
a=[[5]*n for _ in range(n)]
q=[[deque()for _ in range(n)]for _ in range(n)]
for i in range(n):
    add.append(list(map(int,input().split())))
for i in range(m):
    x, y, z = map(int,input().split())
    x-=1;y-=1
    q[x][y].append((z))
    cnt+=1
for i in range(k):
    solve()
print(cnt)
