from sys import*
input = stdin.readline
def solve(pos, cnt):
    ans=INF
    if cnt > n//2 or pos==n: return ans       #완탐해도 이런거 쳐내주기(처음에 이거 안해서 시간초과뜸)
    t1, t2 = 0, 0
    if cnt == n//2:
        for i in range(n):
            for j in range(i):
                if check[i] and check[j]:
                    t1 += a[i][j] + a[j][i]
                elif not(check[i] or check[j]):
                    t2 += a[i][j] + a[j][i]
        ans = abs(t1-t2)
        return ans
    check[pos]=1
    ans = min(ans, solve(pos+1, cnt+1))
    check[pos]=0
    ans = min(ans, solve(pos+1, cnt))
    return ans
INF=1e9
n=int(input())
a=[list(map(int,input().split()))for _ in range(n)]
check=[0]*n
print(solve(0,0))
