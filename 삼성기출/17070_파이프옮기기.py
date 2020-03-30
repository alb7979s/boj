#똑같은 로직 c++은 통과, python 시간초과 뜸, dp로 다시 풀기
from sys import*
from collections import*
input = lambda:stdin.readline().strip()

def checkD(dx, dy):
    if dx:
        if dy: return 2
        else: return 1
    else:
        return 0        #세가지 경우밖에 없음, dx==0이면 dy=1임
dd=[[(0,1), (1,1)],             #옆 방향
    [(1,0), (1,1)],             #아래
    [(0,1), (1,0), (1,1)]]      #대각선
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
q=deque()
q.append((0,1,0))   #x, y, d
cnt = 0
while q:
    x, y, d = q.popleft()
    if x==n-1 and y==n-1:
        cnt+=1
        continue
    for dx, dy in dd[d]:
        nx, ny, nd = x+dx, y+dy, checkD(dx, dy)
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny] or (nx == n-1 and nd==1) or (ny==n-1 and nd==0): continue
        if nd==2:
            if a[x][ny] or a[nx][y]: continue
        q.append((nx, ny, nd))
print(cnt)
