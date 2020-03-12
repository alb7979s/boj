#문제 집중해서 읽기, 궁수 성 있는곳에만 위치하는건데 괜히 n*m 모든 위치 확인할뻔
from heapq import*
def solve(pos, cnt):
    global a
    res=0
    if pos == m or cnt>3:
        if cnt == 3:
            res = max(res, cal())
            a=[x[:]for x in b]
        return res
    arrow.append((n, pos))
    res = max(res, solve(pos+1, cnt+1))
    arrow.pop()
    res = max(res, solve(pos+1, cnt))
    return res
def cal():
    dieCnt=0;totalCnt=0
    while 1:
        die=[]
        if totalCnt == enermy: return dieCnt
        for x, y in arrow:
            pq=[]; visit=[[0]*m for _ in range(n)]
            heappush(pq,(1, y, x-1))
            visit[x-1][y]=1
            while(pq):
                d, y, x = heappop(pq)
                if a[x][y]==1:
                    if (x,y) not in die:
                        die.append((x,y))
                    break
                for dx, dy in dd:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visit[nx][ny] or d>=D: continue
                    heappush(pq,(d+1, ny, nx))
                    visit[nx][ny]=1
        for x, y in die:
            a[x][y]=0
            dieCnt+=1
            totalCnt+=1
        for i in range(m):
            for j in range(n-1,-1,-1):
                if a[j][i] and j==n-1:
                    a[j][i]=0
                    totalCnt+=1
                elif a[j][i]:
                    a[j+1][i] = a[j][i]
                    a[j][i] = 0
dd=[(-1,0),(0,1),(1,0),(0,-1)]
n,m,D=map(int,input().split())
a=[]
enermy=0
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(m):
        if a[i][j]: enermy+=1
b=[x[:]for x in a]
arrow=[]
print(solve(0,0))
