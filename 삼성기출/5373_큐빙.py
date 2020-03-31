#sides 수정해야함 반대 방향으로 돌려버림
from sys import*
input = lambda: stdin.readline().strip()
sides = [[[0, 3, 1, 4, 2, 5],   #오른 회전의 U, D
          [3, 1, 0, 5, 4, 2],   #F, B
          [4, 0, 2, 3, 5, 1]],  #L, R
         [[0, 2, 4, 1, 3, 5],   #왼 회전의 U, D
          [2, 1, 5, 0, 4, 3],   #F, B
          [1, 5, 2, 3, 0, 4]]]  #L, R
direc='UFLRBD'
color='wrgboy'
def move(d, t):
    global a
    b=[x[:]for x in a]
    t = 0 if t == '+' else 1    #리스트 인덱스 쓸거라 돌리는 곳(오른쪽, 왼쪽) 숫자로 바꿔줌
    d = direc.index(d)          #얘도 인덱스 쓸거라 돌리는 방향(상,하,앞,뒤,좌,우) 숫자로 바꿔줌
    for i in range(6):
        for j in range(3):
            if d==0 or d==5:    #U, D
                fix = 0 if d==0 else 2    #고정 값 선언
                b[i][fix][j] = a[sides[t][0][i]][fix][j]    #a값 말고 다른곳에 저장해야 데이터 손실안남 일단 짜고 고치기
            elif d==2 or d==3:  #L, R
                fix = 0 if d==2 else 2
                b[i][j][fix] = a[sides[t][2][i]][j][fix]
    if d==1:  #F, B 얘는 고정값이 바껴서 따로 처리함
        for i in range(3):
            b[0][2][i] = a[sides[t][1][0]][i][0]
            b[5][2][i] = a[sides[t][1][5]][i][0]
            b[2][i][0] = a[sides[t][1][2]][2][i]
            b[3][i][0] = a[sides[t][1][3]][2][i]
    elif d==4:
        for i in range(3):
            b[0][0][i] = a[sides[t][1][0]][i][2]
            b[5][0][i] = a[sides[t][1][5]][i][2]
            b[2][i][2] = a[sides[t][1][2]][0][i]
            b[3][i][2] = a[sides[t][1][3]][0][i]
    a=[x[:] for x in b]
for tc in range(int(input())):
    n=int(input())
    string_list=list(map(str, input().split()))
    a=[[[i for _ in range(3)] for _ in range(3)]for i in range(6)]  #UFLRBD
    for x in string_list:
        move(x[0], x[1])    #방향, 도는곳
    for i in range(3):
        for j in range(3):
            print(color[a[0][i][j]],end='')
        print()
