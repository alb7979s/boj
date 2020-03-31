def rotate(r, c, s):
    global b
    for i in range(s+1):
        x, y = r-i, c-i
        temp = b[x][y]
        for dx, dy in dd:
            for j in range(i*2):
                nx, ny = x+dx, y+dy
                b[nx][ny], temp = temp, b[nx][ny]
                x, y = nx, ny
def solve(cnt):
    global b
    res = INF
    if cnt == k:
        b = [x[:]for x in a]
        for t in turn:
            r, c, s = rotate_list[t]
            rotate(r, c, s)
        for i in range(n):
            res = min(res, sum(b[i]))
        return res
    for i in range(k):
        if visit[i]: continue
        visit[i] = 1
        turn.append(i)
        res = min(res, solve(cnt+1))
        visit[i] = 0
        turn.pop()
    return res
INF=1e9
dd=[(0,1), (1,0), (0,-1), (-1,0)]
n,m,k=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
b=[]
turn = []
rotate_list = []
visit=[0]*k
for i in range(k):
    r, c, s = map(int,input().split())
    rotate_list.append((r-1, c-1, s))
print(solve(0))
