from heapq import*
k,n=map(int,input().split())
a=list(map(int,input().split()))
pq=[]
for i in range(k):
    heappush(pq, a[i])

prev = -1
for i in range(n-1):
    cur = heappop(pq)
    for j in range(k):
        temp = cur * a[j]
        if temp < (1<<31): heappush(pq, temp)
        else: break
    prev = cur
    while prev == pq[0]:
        heappop(pq)
print(pq[0])
