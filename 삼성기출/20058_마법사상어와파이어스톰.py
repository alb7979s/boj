from sys import*
from collections import*
input = lambda:stdin.readline().strip()
def bfs(x, y):
    global total
    q = deque()
    q.append((x, y))
    visit[x][y] = 1
    total += board[x][y]
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0,1), (0,-1), (-1,0), (1,0)]:
            nx, ny = x+dx, y+dy
            if nx<0 or ny < 0 or nx > n-1 or ny > n-1 \
               or (not board[nx][ny]) or visit[nx][ny]: continue
            visit[nx][ny]=1
            total += board[nx][ny]
            q.append((nx,ny))
            cnt += 1
    return cnt
def rotate(p):
    for x in range(0, n, p):
        for y in range(0, n, p):
            temp = [[0]*p for _ in range(p)]
            for i in range(p):
                for j in range(p):
                    temp[j][(p-i-1)] = board[x+i][y+j]
            for i in range(p):
                for j in range(p):
                    board[x+i][y+j] = temp[i][j]
def melt():
    visit = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            cnt = 0
            if not board[x][y]: continue
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx = x+dx
                ny = y+dy
                if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 or not board[nx][ny]: continue
                cnt += 1
            if cnt < 3: visit[x][y] = 1
    for x in range(n):
        for y in range(n):
            if visit[x][y]: board[x][y]-=1
def printf():
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()
n, t = map(int,input().split())
n = 1 << n
board = [list(map(int,input().split()))for _ in range(n)]
commands = list(map(int,input().split()))
for command in commands:
    rotate(1<<command)
    melt()
visit = [[0]*n for _ in range(n)]
maxComponent = 0
total = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j] and board[i][j]:
            maxComponent = max(maxComponent, bfs(i, j))
print(total)
print(maxComponent)

