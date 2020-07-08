#https://www.acmicpc.net/problem/1658
#MAX값 커지면 아래처럼 dict 이용해줘야함
#양방향 => c[u][v]=value, c[v][u]=value
#단방향 => c[u][v]=value, c[v][u]=0
#유량 흐를때 반대로 흐르는거 계산해주려면 단방향이여도 반대방향 adj이어줘야함
from sys import *
from collections import *
input = stdin.readline
n, m = map(int, input().split())
MAX = (n+1) * m + 2
s, e = MAX - 2, MAX - 1
INF = 1e9
adj = [[] for _ in range(MAX)]
c = {}
f = {}
a = list(map(int, input().split()))
def cfAdd(u, v, value):
    c[u, v] = value
    c[v, u] = 0
    f[u, v] = 0
    f[v, u] = 0
def edgeAdd(u, v):
    adj[u].append(v)
    adj[v].append(u)

# 그래프 간선 추가
for i in range(len(a)):
    edgeAdd(s, i)
    cfAdd(s, i, a[i])
for day in range(m):
    b = list(map(int, input().split()))
    eprev = n * m + day
    edgeAdd(eprev, e)
    cfAdd(eprev, e, b[-1])
    if day != m - 1:
        for i in range(n):
            u = (day * n) + i
            v = (day + 1) * n + i
            edgeAdd(u, v)
            cfAdd(u, v, INF)
    for i in range(1, b[0] + 1):
        u = (day * n) + b[i] - 1
        edgeAdd(u, eprev)
        cfAdd(u, eprev, INF)
        if day != m - 1:
            for j in range(1, b[0] + 1):
                v = (day + 1) * n + b[j] - 1
                try:
                    if c[u, v]: continue
                except:
                    pass
                edgeAdd(u, v)
                cfAdd(u, v, INF)
# 애드몬드카프
total = 0
while 1:
    q = deque()
    q.append(s)
    prev = [-1] * MAX
    prev[s] = s
    while q and prev[e] == -1:
        u = q.popleft()
        for v in adj[u]:
            if prev[v] == -1 and c[u, v] - f[u, v] > 0:  # 여유 용량이 남아있는경우
                prev[v] = u
                q.append(v)
    if prev[e] == -1:
        print(total)
        break
    flow = INF
    v = e
    while v != s:
        u = prev[v]
        flow = min(flow, c[u, v] - f[u, v])
        v = u
    v = e
    while v != s:
        u = prev[v]
        f[u, v] += flow
        f[v, u] -= flow
        v = u
    total += flow
