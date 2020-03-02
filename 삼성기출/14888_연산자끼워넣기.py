def solve(pos, res):
    global MAX, MIN
    if pos == n:
        MAX = max(MAX, res)
        MIN = min(MIN, res)
        return
    if b[0]>0:
        b[0]-=1
        solve(pos+1, res+a[pos])
        b[0]+=1
    if b[1]>0:
        b[1]-=1
        solve(pos+1, res-a[pos])
        b[1]+=1
    if b[2]>0:
        b[2]-=1
        solve(pos+1, res*a[pos])
        b[2]+=1
    if b[3]>0:
        b[3]-=1
        solve(pos+1, int(res/a[pos]))
        b[3]+=1
    return
INF=1e9
MAX = -INF;
MIN = INF
n=int(input())
a=list(map(int,input().split()))    #숫자
b=list(map(int,input().split()))    #연산 개수, + - * / 순
solve(1, a[0])
print(MAX)
print(MIN)
