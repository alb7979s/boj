from sys import*
from collections import*
input = stdin.readline
def scope(nx, ny):
    if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]==2: return 1
    return 0
def searchD(dx, dy):
    for i in range(4):
        if -dx == dd[i][0] and -dy == dd[i][1]: return i
def solve():
    for turn in range(1,1001):
        for i in range(k):
            x, y = horse[i]
            for j in range(len(v[x][y])):
                if v[x][y][j][0] == i:
                    s=j
                    break
            d=v[x][y][s][1]
            dx, dy = dd[d]
            nx, ny = x+dx, y+dy
            if scope(nx, ny):   #범위 밖 or 파랑
                nx, ny = x-dx, y-dy
                d = searchD(dx, dy)
                v[x][y][s][1]=d
                if scope(nx, ny): continue
            if a[nx][ny]==0:    #흰색
                temp=[]
                for j in range(len(v[x][y])-s):
                    temp.append(v[x][y].pop())
                while temp:
                    hi, d = temp.pop()
                    horse[hi] = [nx, ny]
                    v[nx][ny].append([hi, d])
            elif a[nx][ny]==1:  #빨강
                for j in range(len(v[x][y])-s):
                    hi, d = v[x][y].pop()
                    horse[hi] = [nx, ny]
                    v[nx][ny].append([hi, d])
            if len(v[nx][ny])>=4: return turn
    return -1
                
dd=[(0,1),(0,-1),(-1,0),(1,0)]  #RLUD
n,k = map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
horse=[]
v=[[[]for _ in range(n)]for _ in range(n)]
for i in range(k):
    x, y, d = map(int,input().split())
    horse.append([x-1, y-1])
    v[x-1][y-1].append([i, d-1])
print(solve())
