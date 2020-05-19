#시간초과 뜸 수정하기

from sys import*
input = stdin.readline

def check(x, y, pos):
    if colored_paper[pos] <= 0: return 0
    for i in range(x, x+pos+1):
        for j in range(y, y+pos+1):
            if i>9 or j>9 or not a[i][j]: return 0
    for i in range(x, x+pos+1):      #색종이 덮기
        for j in range(y, y+pos+1):
            a[i][j]=0
    return 1

def solve(pos, cnt, covered):
    global a, res
    if covered == one_cnt: return cnt
    if pos == one_cnt or res<=cnt: return res
    x, y = one_list[pos]
    if a[x][y]:
        for i in range(5):
            if check(x,y,i):
                colored_paper[i]-=1
                res = min(res, solve(pos+1, cnt+1, covered+(i+1)**2))
                colored_paper[i]+=1
                for n in range(x, x+i+1):       
                    for m in range(y, y+i+1):
                        a[n][m]=1
                #res = min(res, solve(pos+1, cnt, covered)) 불필요함, 시간초과 원인
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
