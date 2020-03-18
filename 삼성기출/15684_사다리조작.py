from sys import*
input = stdin.readline
def check():
    for i in range(m):
        s = i
        for j in range(n):
            if a[j][s]: s+=1
            elif s-1 >=0 and a[j][s-1]: s-=1
        if s != i: return 0
    return 1
def solve(cnt, x, y):
    res = INF
    if cnt>3: return res
    if check(): return cnt
    if cnt == 3: return res     #여기부분 
    for i in range(x, n):       #여기부분 시간초과 원인
        temp = y if x==i else 0
        for j in range(temp, m-1):
            if a[i][j]:
                j+=1
            else:
                a[i][j]=1
                res = min(res, solve(cnt+1, i, j))
                a[i][j]=0
    return res

INF = 1e9
m,k,n = map(int,input().split())
a=[[0]*m for _ in range(n)]
for i in range(k):
    x, y = map(int,input().split())
    a[x-1][y-1] = 1
ans=solve(0,0,0)
print(ans if ans != INF else -1)
