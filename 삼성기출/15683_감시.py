from sys import*
from collections import*
input = lambda:stdin.readline().strip()
dd=[(-1,0),(0,1),(1,0),(0,-1)]  #URDL
U,R,D,L = 1<<0, 1<<1, 1<<2, 1<<3    #비트 마스크 + 집합으로 처리 할거
cctv = [[0],
        [U,R,D,L],                      #1
        [U|D, L|R],                     #2
        [U|R, R|D, D|L , L|U],          #3
        [U|R|D, R|D|L, D|L|U, L|U|R],   #4
        [U|R|D|L]]                      #5
def solve(pos, res):
    global a
    ans=0
    if pos == len(cctv_list):return res
    b=[x[:]for x in a]  #a리스트 b에 저장해놓음
    x, y, num = cctv_list[pos]
    for c in cctv[num]: #방향 원소들
        ans = max(ans, solve(pos+1, res+cal(x,y,c)))
        a=[x[:]for x in b]
    return ans
def cal(x, y, c):
    cnt=0
    for i in range(4):
        if c & (1<<i):      #찾을 방향이랑 찾을cctv원소랑 교집합이면
            dx, dy = dd[i]
            nx, ny = x, y
            while 1:
                nx, ny = nx+dx, ny+dy
                if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or a[nx][ny] == 6:break
                if not a[nx][ny]: cnt+=1
                a[nx][ny]=9
    return cnt
n,m=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)] #0빈 칸, 1~5 CCTV 종류
cctv_list=[]; zero=0
for i in range(n):
    for j in range(m):
        if 1 <= a[i][j] <= 5:
            cctv_list.append((i,j,a[i][j]))
        elif not a[i][j]:
            zero+=1
print(zero - solve(0, 0))
