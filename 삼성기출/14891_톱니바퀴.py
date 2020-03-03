from sys import*
from collections import*
input = lambda:stdin.readline().strip()
def turn(x, d):
    check[x]=d          #방향 d로 check해줘야는디 처음에 무의식적으로 1로 체크해서 틀렸었음
    if x+1<4 and not check[x+1]:
        if a[x][2] != a[x+1][-2]:
            turn(x+1, -d)
    if x-1 >= 0 and not check[x-1]:
        if a[x-1][2] != a[x][-2]:
            turn(x-1, -d)
def rotate():
    for i in range(4):
        if check[i]==1: #시계방향 회전
            prev = a[i][-1]
            for j in range(8):
                a[i][j], prev = prev, a[i][j]
        elif check[i]==-1:
            prev = a[i][0]
            for j in range(8):
                a[i][-(j+1)], prev = prev, a[i][-(j+1)]

a=[list(input())for _ in range(4)]
k=int(input())
for i in range(k):
    x, d = map(int,input().split())
    check=[0]*4
    turn(x-1, d)
    rotate()
res=0
for i in range(4):
    if int(a[i][0]): res+=(1<<i)
print(res)
