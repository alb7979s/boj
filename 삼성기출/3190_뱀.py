from sys import*
from collections import*
input = stdin.readline
n=int(input())
k=int(input())
a=[[0]*n for _ in range(n)]
for i in range(k):
    r, c = map(int,input().split())
    a[r-1][c-1] = 1
l = int(input())
turn=deque()
for i in range(l):
    x, c = map(str,input().split())
    turn.append((int(x),c))

def scope(nx, ny):
    if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]==2: return 0
    return 1
a[0][0] = 2     #사과 1, 뱀 2
dd=[(0,1),(1,0),(0,-1),(-1,0)]  #R, D, L, U
nx, ny, d, t = 0, 0, 0, 0
tail=deque()
tail.append((0,0))
while 1:
    if turn and turn[0][0]==t:
        x, c = turn.popleft()
        if c=='L': d = (d+3)%4
        else: d = (d+1)%4      
    dx, dy = dd[d]
    nx, ny = nx+dx, ny+dy
    if not scope(nx,ny):
        print(t+1); break
    if a[nx][ny] == 0:
        t1,t2 = tail.popleft()
        a[t1][t2] = 0
    tail.append((nx,ny))
    a[nx][ny]=2
    t+=1
