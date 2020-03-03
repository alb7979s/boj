#치킨 거리 abs(x1-x2) + abs(y1-y2)
#m개 골라서 치킨거리 가장 작게되는 값
from sys import*
from collections import*
input = stdin.readline
def solve(pos, cnt):    #여기서 pos 치킨집 인덱스임
    ans=INF
    if cnt > m: return ans
    if pos == len(chicken):
        res = 0
        if cnt == m:    #최대m개인데 어차피 m개 일 때가 제일 작게 만들 수 있음
            for x, y in house:
                MIN = INF
                for cx, cy in temp:
                    MIN = min(MIN, abs(x-cx)+abs(y-cy))
                res+=MIN
        return res if res!=0 else INF
    temp.append((chicken[pos]))
    ans = min(ans, solve(pos+1, cnt+1))
    temp.pop()
    ans = min(ans, solve(pos+1, cnt))
    return ans
INF = 1e9
n,m = map(int,input().split())  #n*n 리스트에서, m개 선택
a, house, chicken, temp = [], [], [], []
for i in range(n):
    a.append(list(map(int,input().split())))
    for j in range(n):
        if a[i][j]==1:  #집
            house.append((i,j))
        elif a[i][j]==2: #치킨집
            chicken.append((i,j))
print(solve(0,0))
