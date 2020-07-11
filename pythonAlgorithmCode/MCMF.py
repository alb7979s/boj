#https://www.acmicpc.net/problem/11405
#flow 반대쪽 음의양 흘려줘야해서 음수 계산할 최단거리 알고리즘 필요
#따라서 벨만포드 쓰는데, 벨만포드 좀 더 개선한 SPFA 사용
from sys import*
from collections import*
input=stdin.readline
def edgeAdd(u, v):
    adj[u].append(v)
    adj[v].append(u)
def SPFA(): 
    prev=[-1]*MAX
    q=deque([s])
    dist=[INF]*MAX
    inq=[False]*MAX
    dist[s]=0
    prev[s]=s
    while q:
        u = q.popleft()
        inq[u] = False
        for v in adj[u]:
            if c[u][v]-f[u][v]>0 and dist[v] > dist[u]+d[u][v]:
                dist[v] = dist[u]+d[u][v]
                prev[v] = u
                if not inq[v]:
                    q.append(v)
                    inq[v]=True
    return prev
def MCMF(prev):
    res=0
    flow=INF
    v = e
    while v!=s:
        u = prev[v]
        flow = min(flow, c[u][v]-f[u][v])
        v = u
    v = e
    while v!=s:
        u = prev[v]
        res += d[u][v]*flow
        f[u][v] += flow
        f[v][u] -= flow
        v = u
    return res
n,m=map(int,input().split())    #m서점(u), n사람(v)
MAX = n+m+2
INF=1e9
s, e = MAX-2, MAX-1
adj=[[]for _ in range(MAX)]
c=[[0]*MAX for _ in range(MAX)]
f=[[0]*MAX for _ in range(MAX)]
d=[[0]*MAX for _ in range(MAX)]
a=list(map(int,input().split()))    #사려는 개수
for u in range(n):
    v = u+m
    edgeAdd(v,e)
    c[v][e]=a[u]
a=list(map(int,input().split()))    #책의 개수
for u in range(m):
    edgeAdd(s, u)
    c[s][u]=a[u]
for i in range(m):
    a=list(map(int,input().split()))
    for j in range(n):
        u = i
        v = j+m
        d[u][v]=a[j]
        d[v][u]=-a[j]
        c[u][v]=INF
        edgeAdd(u,v)
ans=0
while 1:
    prev = SPFA()
    if prev[e]==-1: break
    ans += MCMF(prev)
print(ans)
