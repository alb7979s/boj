#이분매칭
#https://www.acmicpc.net/problem/1298
from sys import*
input=stdin.readline
def dfs(a):
    if visit[a]==visitCnt:
        return False
    visit[a] = visitCnt
    for b in adj[a]:
        if B[b]==-1 or dfs(B[b]):
            A[a]=b
            B[b]=a
            return True
    return False
        
n,m=map(int,input().split())
adj=[[]for _ in range(n)]
A=[-1]*n
B=[-1]*n
visit=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    a-=1;b-=1
    adj[a].append(b)
match=0
visitCnt=1
for i in range(n):
    match+=dfs(i)
    visitCnt+=1
print(match)
