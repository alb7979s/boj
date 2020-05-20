#이렇게 복잡하게 풀 문젠가 싶기도 하고..
from sys import*
from collections import*
input = stdin.readline
def bfs(red):
    redSum, blueSum, otherResions, redResion = 0, 0, 0, 0
    rq, oq = deque(), deque()
    for i in range(n):
        if red & (1<<i):
            if not rq: rq.append(i)
            redSum += people[i]
            redResion |= (1<<i) 
        else:
            if not oq: oq.append(i)
            blueSum += people[i]
            otherResions |= (1<<i)
    if not(redSum and blueSum): return INF
    while rq:
        x = rq.popleft()
        redResion &= ~(1<<x)
        for nx in adj[x]:
            if redResion & (1<<nx) and red & (1<<nx):
                rq.append(nx)
    while oq:
        x = oq.popleft()
        otherResions &= ~(1<<x)
        for nx in adj[x]:
            if otherResions & (1<<nx) and not (red & (1<<nx)):
                oq.append(nx)
    if redResion or otherResions: return INF
    return abs(redSum - blueSum)
            
def solve(pos, red):
    res=INF
    if pos == n: return bfs(red)
    res = min(res, solve(pos+1, red | (1<<pos)))
    res = min(res, solve(pos+1, red))
    return res
    
INF=1e9
n=int(input())
people=list(map(int,input().split()))
adj=[[]for _ in range(n)]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(1, len(tmp)):
        adj[i].append(tmp[j]-1)
res=solve(0, 0)
visit=[0]*n
print(res if res!=INF else -1)
