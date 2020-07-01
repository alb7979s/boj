#종만북 -> dfs 순회 결과 뒤집은거
#이 코드는 indegree 배열 만들어서 값 0인거 q에 넣고 빼면서 구해줌
#모든 정점 돌동안 큐가 빈다 => 싸이클이라 indegree 값 0인거 부족 => 정렬불가
#2623
n,m=map(int,input().split())
indegree=[0 for _ in range(n)]
adj=[[]for _ in range(n)]
for i in range(m):
    order=list(map(int,input().split()))
    for j in range(order[0]-1):
        indegree[order[j+2]-1]+=1
        adj[order[j+1]-1].append(order[j+2]-1)
q=deque()
for i in range(n):
    if not indegree[i]: q.append(i)
res=[]
for i in range(n):
    if not q:
        print(0)
        exit()
    u = q.popleft()
    res.append(u)
    for v in adj[u]:
        indegree[v]-=1
        if not indegree[v]:
            q.append(v)
for x in res:
    print(x+1)
    
