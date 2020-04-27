#시간초과 뜸 수정하기

from sys import*
input = stdin.readline

def check(x, y, pos):
    if colored_paper[pos] <= 0: return 0
    for i in range(pos+1):
        nx = x+i
        for j in range(pos+1):
            ny = y+j
            if nx>9 or ny>9 or (not a[nx][ny]): return 0
    for i in range(pos+1):      #색종이 덮기
        nx = x+i
        for j in range(pos+1):
            ny = y+j
            a[nx][ny]=0
    return 1

def solve(pos, cnt, covered):
    global a, res
    if covered == one_cnt: return cnt
    if pos == one_cnt or res<=cnt: return res
    x, y = one_list[pos]
    b=[x[:]for x in a]
    if a[x][y]:
        for i in range(5):
            if check(x,y,i):
                colored_paper[i]-=1
                res = min(res, solve(pos+1, cnt+1, covered+(i+1)**2))
                colored_paper[i]+=1
                a=[x[:]for x in b]
                res = min(res, solve(pos+1, cnt, covered))
    else: res=min(res, solve(pos+1, cnt, covered))
    return res
INF=1e9
a=[]
colored_paper=[5]*5
one_cnt=0
one_list=[]
res=INF
for i in range(10):
    a.append(list(map(int,input().split())))
    for j in range(10):
        if a[i][j]:
            one_cnt+=1
            one_list.append((i,j))
ans=solve(0,0,0)
print(ans if ans!=INF else -1)
