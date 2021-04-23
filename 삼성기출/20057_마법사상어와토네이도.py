from sys import*
input = lambda:stdin.readline().strip()

dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]
mul = [.01, .01, .07, .07, .02, .02, .1, .1, .05]
spreadDir = [[(-1,1),(1,1),(-1,0),(1,0),(-2,0),(2,0),(-1,-1),(1,-1),(0, -2)],
             [(-1,-1),(-1,1),(0,-1),(0,1),(0,-2),(0,2),(1,-1),(1,1),(2,0)],
             [(-1,-1),(1,-1),(-1,0),(1,0),(-2,0),(2,0),(-1,1),(1,1),(0,2)],
             [(1,-1),(1,1),(0,-1),(0,1),(0,-2),(0, 2),(-1,-1),(-1,1),(-2,0)]]
def spread(x, y, d):
    out = 0
    totalMove = 0
    for i in range(len(mul)):
        dx, dy = spreadDir[d][i]
        nx = x + dx
        ny = y + dy
        move = int(board[x][y] * mul[i])
        totalMove += move
        if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
            out += move
            continue
        board[nx][ny] += move
    nx = x + dd[d][0]
    ny = y + dd[d][1]
    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
        out += (board[x][y] - totalMove)
    else:
        board[nx][ny] += (board[x][y] - totalMove)
    board[x][y] = 0
    return out
        
def solve(x, y, d):
    res = 0
    length = 0
    total = 2*n - 1
    for i in range(total):
        if(i%2==0 and i!=total-1): length+=1
        dx, dy = dd[d]
        for j in range(length):
            x += dx
            y += dy
            res += spread(x, y, d)
        d = (d+1)%4
    return res
        
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
print(solve(n//2, n//2, 0)) 

