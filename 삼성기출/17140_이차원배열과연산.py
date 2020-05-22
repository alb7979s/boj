from sys import*
from collections import*
input = stdin.readline
def solve():
    global n,m
    for t in range(101):
        if a[r-1][c-1] == k: return t
        if n >= m:
            for i in range(n):
                cnt = [0]*101
                for j in range(m):
                    if a[i][j]:
                        cnt[a[i][j]]+=1
                        a[i][j]=0
                b=[]
                for j in range(101):
                    if cnt[j]:b.append((cnt[j], j))
                b.sort()
                m = max(m, len(b)*2)
                j=0
                for x in b:
                    a[i][j+1], a[i][j] = x
                    j+=2
        else:
            for i in range(m):
                cnt = [0]*101
                for j in range(n):
                    if a[j][i]:
                        cnt[a[j][i]]+=1
                        a[j][i]=0
                b=[]
                for j in range(101):
                    if cnt[j]:b.append((cnt[j], j))
                b.sort()
                n = max(n, len(b)*2)
                j=0
                for x in b:
                    a[j+1][i], a[j][i] = x
                    j+=2
    return -1
r,c,k = map(int,input().split())
a=[[0]* 101 for _ in range(101)]
for i in range(3):
    a[i][0], a[i][1], a[i][2] = map(int,input().split())
n, m = 3, 3
print(solve())
