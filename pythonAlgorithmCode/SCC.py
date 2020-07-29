#2150
#SCC
from sys import*
input=stdin.readline
setrecursionlimit(10**6)
def dfs(u):
    global cnt, SN
    dfsn[u] = cnt
    cnt += 1
    s.append(u)

    res = dfsn[u]
    for v in adj[u]:
        #방문 x
        if(dfsn[v]==0): res = min(res, dfs(v))
        #방문 했으나 SCC 추출 x
        if(not finished[v]): res = min(res, dfsn[v])

    if res == dfsn[u]:
        curSCC = []
        while 1:
            t = s.pop()
            curSCC.append(t)
            finished[t] = True
            sn[t] = SN      #sn: i가 속한 SCC번호
            if(t==u): break
        curSCC.sort()
        SCC.append(curSCC)
        SN+=1
    return res
V, E = map(int,input().split())
adj = [[]*V for _ in range(V)]
SCC, s = [], []
dfsn, finished, sn = [0]*V, [0]*V, [0]*V
SN, cnt = 1, 1
for i in range(E):
    a,b = map(int,input().split())
    adj[a-1].append(b-1)
#DFS돌며 SCC 추출
for i in range(V):
    if(not dfsn[i]): dfs(i)
SCC.sort()
print(len(SCC))
for scc in SCC:
    for x in scc:
        print(x+1, end=' ')
    print(-1)
