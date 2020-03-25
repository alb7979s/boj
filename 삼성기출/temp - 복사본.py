from sys import*
input = stdin.readline
def solve(pos, score):  #pos -> 몇 번째 주사위인지
    global horse, visit
    res = 0
    if pos == 10:
        return score
    b = [x[:] for x in horse]
    c = [x[:] for x in visit]
    for i in range(4):
        d, x = horse[i]
        if x == INF or (len(visit[d]) > x+dice[pos] and visit[d][x+dice[pos]]): continue    #이미 도착 했거나 말 있는곳
        res = max(res, solve(pos+1, score + move(i, dice[pos])))
        horse=[x[:] for x in b]
        visit=[x[:] for x in c]
    return res

def move(i, x):
    d, idx = horse[i]           #방향, 인덱스
    if d==0 and (idx in inside):#d가 0이고(테두리), 확인할 index가 내부에 들어갈 인덱스면
        nd = idx // 5           #만약 5면 d=1, 10이면 d=2, ...
        nx = x
    else:                       #원래 방향대로 감
        nd = d
        nx = x + idx
    if len(a[nd]) <= nx:    #도착
        horse[i] = [0, INF]
        visit[d][x]=0
        return 0
    visit[nd][nx] = 1
    visit[d][x] = 0
    horse[i] = [nd, nx]
    return a[nd][nx]

a=[[2*i for i in range(21)]]             # a[0] => 테두리
a.append([10, 13, 16, 19, 25, 30, 35, 40])  # a[1] => 5번째칸 갈 시 이동방향
a.append([20, 22, 24, 25, 30, 35, 40])      # a[2] => 10번째칸 갈 시 이동방향
a.append([30, 28, 27, 26, 25, 30, 35, 40])  # a[3] => 15번째칸 갈 시 이동방향
inside = [5, 10, 15]            #내부로 들어가야 하는 index 모음

INF = 1e9
dice = list(map(int,input().split())) #이동할 주사위 정보
visit=[[0]*21 for _ in range(4)]#1차:방향, 2차:인덱스
horse=[[0,0] for _ in range(4)] #1차:말 번호, 2차: [방향, 인덱스]
print(solve(0, 0))
