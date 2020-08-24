#Minimum Spanning Tree (kruskal)
#https://www.acmicpc.net/problem/1647
from sys import*
input = stdin.readline
setrecursionlimit(10**6)
def find(u):
    if parent[u] == u: return u
    parent[u] = find(parent[u])
    return parent[u]
def union(u, v):
    u = find(u)
    v = find(v)
    parent[u] = v
n,m=map(int,input().split())
parent=list(range(n+1))
info=[]
for i in range(m):
    a,b,c=map(int,input().split())
    info.append((a,b,c))
info.sort(key = lambda x: x[2])
res=0
MAX=0
for a,b,c in info:
    a = find(a)
    b = find(b)
    if a!=b:
        res+=c
        MAX = max(MAX, c)
        union(a,b)
print(res-MAX)
