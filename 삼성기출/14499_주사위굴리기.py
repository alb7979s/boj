from sys import*
input = stdin.readline
n,m,x,y,k=map(int,input().split())
a=[];dice=[0]*6
dd=[(0,0),(0,1),(0,-1),(-1,0),(1,0)]    #1번부터 RLUD
direct = [[0],                  #0이 바닥, 5천장으로 고정했을때 바뀌는 방향들
          [2, 1, 5, 0, 4, 3],
          [3, 1, 0, 5, 4, 2],
          [1, 5, 2, 3, 0, 4],
          [4, 0, 2, 3, 5, 1]]
for i in range(n):
    a.append(list(map(int,input().split())))
move = list(map(int,input().split()))

#0바닥, 5천장
temp=[0]*6
for d in move:
    dx, dy = dd[d]
    nx, ny = x+dx, y+dy
    if nx<0 or ny<0 or nx>n-1 or ny>m-1: continue
    for i in range(6):
        temp[i] = dice[direct[d][i]]
    for i in range(6):
        dice[i] = temp[i]
    if a[nx][ny]:
        dice[0] = a[nx][ny]
        a[nx][ny] = 0
    else:
        a[nx][ny] = dice[0]
    x, y = nx, ny
    print(dice[5])
