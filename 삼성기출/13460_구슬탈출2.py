from sys import*
from collections import*
input = lambda: stdin.readline().strip()
def move(x, y, dx, dy):
    d=0
    while 1:
        x, y = x+dx, y+dy
        d+=1
        if a[x][y] == '#': return (x-dx, y-dy, d-1)
        elif a[x][y] == 'O': return (x, y, d)
def bfs():
    global q
    while q:
        rx, ry, bx, by = q.popleft()
        if visit[rx][ry][bx][by] > 10: break
        if a[rx][ry] == 'O': return visit[rx][ry][bx][by]       #이거 아래부분에서 visit[][][][]+1로 했었는데 11버째 되는거때문에 틀림떴었음
        for dx, dy in dd:
            nrx, nry, rd = move(rx, ry, dx, dy)
            nbx, nby, bd = move(bx, by, dx, dy)
            if a[nbx][nby] == 'O': continue
            if nrx == nbx and nry == nby:
                if rd > bd:
                   nrx, nry = nrx-dx, nry-dy
                else:
                    nbx, nby = nbx-dx, nby-dy
            if visit[nrx][nry][nbx][nby] != -1: continue
            visit[nrx][nry][nbx][nby] = visit[rx][ry][bx][by]+1
            q.append((nrx, nry, nbx, nby))
    return -1
n,m = map(int,input().split())
a=[]
for i in range(n):
    a.append(input())
    for j in range(m):
        if a[i][j] == 'R':
            rx, ry = i, j
        elif a[i][j] == 'B':
            bx, by = i, j
visit = [[[[-1]*m for _ in range(n)]for _ in range(m)]for _ in range(n)]
visit[rx][ry][bx][by]=0
dd = [(-1,0), (0,1), (1,0), (0,-1)]
q=deque()
q.append((rx, ry, bx, by))
print(bfs())
