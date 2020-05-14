#17779
from sys import*
from collections import*
input = stdin.readline
def scope(x, y, d1=0, d2=0):
    if x<0 or y-d1 < 0 or x+d1+d2 > n-1 or y+d2 > n-1: return 0
    return 1
def zoneFive(x, y, d1, d2):
    check[x][y]=5
    nx, ny = x, y
    for i in range(len(ddd)):
        dx, dy = ddd[i]
        if i==0 or i==2:
            for j in range(d1):
                nx, ny = nx+dx, ny+dy
                check[nx][ny]=5
        else:
            for j in range(d2):
                nx, ny = nx+dx, ny+dy
                check[nx][ny]=5
def zoneCheck(r, c, x, y, d1, d2, zone):
    q=deque()
    q.append((r, c))
    check[r][c]=zone
    while q:
        r, c = q.popleft()
        for dx, dy in dd:
            nx, ny = r+dx, c+dy
            f=False
            if not scope(nx, ny) or check[nx][ny]!=0: continue
            if zone==1:
                if 0 <= nx < x + d1 and 0 <= ny <= y : f=True
            elif zone==2:
                if 0<= nx <= x+d2 and y < ny <= n-1: f=True
            elif zone==3:
                if x + d1 <= nx <= n - 1 and 0 <= ny < y - d1 + d2: f=True
            elif zone==4:
                if x+d2 < nx <= n-1 and y-d1 <= ny <= n-1: f=True
            if f:
                check[nx][ny]=zone
                q.append((nx, ny))
def cal(x, y, d1, d2):
    zoneCheck(0, 0, x, y, d1, d2, 1)
    zoneCheck(0, n-1, x, y, d1, d2, 2)
    zoneCheck(n-1, 0, x, y, d1, d2, 3)
    zoneCheck(n-1, n-1, x, y, d1, d2, 4)
    for r in range(n):
        for c in range(n):
            if check[r][c]==0:
                group[4]+=a[r][c]
            else:
                group[check[r][c]-1]+=a[r][c]
    MAX = -INF
    MIN = INF
    for i in range(5):
        MAX = max(MAX, group[i])
        MIN = min(MIN, group[i])
    return MAX-MIN
def solve():
    global group, check
    res=INF
    for x in range(n):
        for y in range(n):
            for d1 in range(1, n):
                if not scope(x, y, d1): break
                for d2 in range(1, n):
                    if not scope(x, y, d1, d2): break
                    group=[0]*5
                    check=[[0]*n for _ in range(n)]
                    zoneFive(x, y, d1, d2)
                    res = min(res, cal(x, y, d1, d2))
    return res
INF=1e9
dd=[(-1,0), (1,0), (0,-1), (0,1)]
ddd=[(1, -1), (1, 1), (-1, 1), (-1, -1)]
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
group=[0]*5
check=[[0]*n for _ in range(n)]
print(solve())
