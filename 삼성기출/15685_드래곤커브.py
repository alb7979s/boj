#드래곤 커브
#1시작 점, 2시작 방향, 3세대
from sys import*
input = stdin.readline
v=[0]
ans=0
MAX = 101
a=[[0]*MAX for _ in range(MAX)]
dd=[(0,1),(-1,0),(0,-1),(1,0)]
#미리 그림
for i in range(11):
    k = 1<<i        #비트연산으로 1,2,4,8, ...(세대 개수=k)
    for j in range(k-1 , -1, -1):
        v.append((v[j]+1)%4)    #뒤로 훑으면서 (+1)%4 = (방향90도)돌려서 저장

for _ in range(int(input())):
    y, x, d, g = map(int,input().split())
    a[x][y]=1
    for i in range(1<<g):   #세대 수 만큼
        dx, dy = dd[(v[i]+d)%4]
        x, y = x+dx, y+dy
        a[x][y]=1

for i in range(100):
    for j in range(100):
        if a[i][j] and a[i+1][j] and a[i][j+1] and a[i+1][j+1]: #사각형이면
            ans+=1
print(ans)
            
