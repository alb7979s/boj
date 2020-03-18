from sys import *
input = stdin.readline
from collections import *
​
def rotate(x, d, k):
   for i in range(x - 1, n, x):
       temp = []
       for j in range(m):
           if d == 1:  # 시계
               temp.append(a[i][(j + k) % m])
           elif d == 0:  # 반시계
               temp.append(a[i][(m + j - k) % m])
       a[i] = temp[:]
​
def bfs(x, y):
   q = deque()
   q.append((x, y))
   visit[x][y] = 1
   f = 0
   while q:
       x, y = q.popleft()
       for dx, dy in dd:
           nx, ny = x + dx, y + dy
           ny %= m                     #열의 처음, 끝 같은지도 확인해줘야 하므로 ny끝에 다다르면 %m 연산으로 처리
           if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1 or visit[nx][ny] or \
                   a[x][y] != a[nx][ny] or a[nx][ny] == 0: continue
           q.append((nx, ny))
           visit[nx][ny] = 1
           f = 1
   if f:
       return 1
   else:#시작할때 visit 체크 해주는데, 같은게 없으면(f==0) 다시 0으로
       visit[x][y] = 0
       return 0
​
def solve(x, d, k):
   flag = 0#인접한 곳에 같은 숫자가 있으면 flag 활성화 시켜줌
   rotate(x, d, k)
   cnt, SUM = 0, 0
   for i in range(n):
       for j in range(m):
           if a[i][j]: cnt += 1
           SUM += a[i][j]
           if not visit[i][j] and a[i][j]:
               if bfs(i, j): flag = 1
   try:
       avg = SUM / cnt     #cnt 없는경우 => 모든 원소 0인 경우
   except:
       return              #종료
   for i in range(n):
       for j in range(m):
           if flag:        #같은게 있으면
               if visit[i][j]: a[i][j] = 0
           else:           #없으면
               if a[i][j] and a[i][j] > avg:
                   a[i][j] -= 1
               elif a[i][j] and a[i][j] < avg:
                   a[i][j] += 1
​
n, m, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dd = [(-1, 0,), (1, 0), (0, -1), (0, 1)]
for i in range(t):
   x, d, k = map(int, input().split())
   visit = [[0] * m for _ in range(n)]
   solve(x, d, k)
ans = 0
for i in range(n):
   ans += sum(a[i])
print(ans)
