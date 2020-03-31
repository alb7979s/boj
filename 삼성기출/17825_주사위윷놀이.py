from sys import*
input = stdin.readline
def solve(pos, score):  #pos -> 몇 번째 주사위인지
    global horse, visit
    res = 0
    if pos == 10:return score
    b = [x[:] for x in horse]
    c = [x[:] for x in visit]
    for i in range(4):
        d, x = horse[i]       #방향, 인덱스
        prev_dice = dice[pos]
        nd = d
        nx = x + prev_dice
        if x == INF: continue
        if d == 0 and (x in [5,10,15]):     #d가 0이고(테두리), 확인할 index가 내부에 들어갈 인덱스면
            nd = x // 5                     #만약 idx가 5면 d=1, 10이면 d=2, ...
            nx = prev_dice
        if nd == 0 and nx == 20:            #d==0, x==20 이랑 d==4, x == 3 이랑 칸 중복되어서 따로 처리
            nd = 4
            nx = 3
        if nd in [1,2,3] and (len(a[nd]) <= nx):   #1,2,3 크기 넘어 갈 때
            nx = nx - len(a[nd])
            nd = 4
        if len(a[nd]) <= nx:                #도착, d=1,2,3일 때 넘은건 위에서 이미 처리됨(21 line)
            horse[i] = [0, INF]
            visit[d][x] = 0
            res = max(res, solve(pos+1, score))
        else:
            if visit[nd][nx]: continue
            horse[i] = [nd, nx]
            visit[nd][nx] = 1
            visit[d][x] = 0
            res = max(res, solve(pos+1, score + a[nd][nx]))
        horse=[x[:] for x in b]
        visit=[x[:] for x in c]
    return res

a=[[2*i for i in range(21)]]             # a[0] => 테두리
a.append([10, 13, 16, 19])  # a[1] => 5번째칸 갈 시 이동방향
a.append([20, 22, 24])      # a[2] => 10번째칸 갈 시 이동방향
a.append([30, 28, 27, 26])  # a[3] => 15번째칸 갈 시 이동방향
a.append([25, 30, 35, 40])  # a[4] => 내부에서 중복되는 놈들 처리 안해주면 visit 방문처리가 잘 안됨

INF = 1e9
dice = list(map(int,input().split())) #이동할 주사위 정보
visit=[[0]*21 for _ in range(5)]#1차:방향, 2차:인덱스
horse=[[0,0] for _ in range(4)] #1차:말 번호, 2차: [방향, 인덱스]
print(solve(0, 0))
