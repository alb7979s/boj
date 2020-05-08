#17779
from sys import*
from collections import*
input = stdin.readline
def scope(x, y, d1=0, d2=0):
    if x<0 or y-d1 < 0 or x+d1+d2 > n-1 or y+d2 > n-1: return 0
    return 1
def zoneFive(x, y, d1, d2):
    q=deque()
    q.append((x, y))
    check[x][y]=5
    while q:
        x, y = q.pop()
        for dx, dy in dd:
            nx, ny = x+dx, y+dy
            if not scope(nx, ny, d1, d2) or check[nx][ny]:continue
            check[nx][ny]=5
            q.append((nx, ny))
def cal(x, y, d1, d2):
    for r in range(n):
        for c in range(n):
            if check[r][c]==5: group[4]+=a[r][c]
            elif 0 <= r < x+d1-1 and 0 <= c <= y-1: group[0]+=a[r][c]
            elif 0<= r <= x+d2-1 and y-1< c <= n-1: group[1]+=a[r][c]
            elif x+d1-1 <= r <= n-1 and 0<= c < y-d1+d2-1: group[2]+=a[r][c]
            elif x+d2-1 < r < n-1 and y-d1-1 <= c <= n-1: group[3]+=a[r][c]
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
            for d1 in range(1, n-y):
                if not scope(x, y, d1): break
                for d2 in range(1, n-y):
                    if not scope(x, y, d1, d2): break
                    group=[0]*5
                    check=[[0]*n for _ in range(n)]
                    zoneFive(x, y, d1, d2)
                    res = min(res, cal(x, y, d1, d2))
    return res
INF=1e9
dd=[(-1,0), (1,0), (0,-1), (0,1)]
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
group=[0]*5
check=[[0]*n for _ in range(n)]
print(solve())
