from sys import*
from collections import*
input = lambda: stdin.readline().strip()
def move(d, t):
    for _ in range(t):  #시계 1번, 반시계 3번
        q=deque()
        for i in range(12):
            q.append(arr[change[d][i]])
        for i in range(12):
            arr[change[d][i]] = q[(i+3)%12]

        for i in range(3):
            for j in range(3):
                temp[j][2-i] = arr[cube[d][i][j]]
        for i in range(3):
            for j in range(3):
                arr[cube[d][i][j]] = temp[i][j]
color = 'wyrogb'
cube_order='UDFBLR'
temp = [[0]*3 for _ in range(3)]
change=[[18, 19, 20, 45, 46, 47, 27, 28, 29, 36, 37, 38],   #U
        [24, 25, 26, 42, 43, 44, 33, 34, 35, 51, 52, 53],   #D
        [6, 7, 8, 44, 41, 38, 11, 10, 9, 45, 48, 51],      #F
        [36, 39, 42, 2, 1, 0, 53, 50, 47, 15, 16, 17],       #B
        [0, 3, 6, 35, 32, 29, 9, 12, 15, 18, 21, 24],       #L
        [11, 14, 17, 33, 30, 27, 2, 5, 8, 20, 23, 26]]      #R
dd=[(0,1),(1,0),(0,-1),(-1,0)]
for tc in range(int(input())):
    n=int(input())
    a=list(map(str, input().split()))
    arr=[i for i in range(54)]
    for i in range(6):
        for j in range(9):
            arr[(i*9)+j] = i
    cube = [[[0] * 3 for _ in range(3)] for _ in range(6)];
    t = 0
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube[i][j][k]=t
                t+=1
    for x in a:
        move(cube_order.index(x[0]), 1 if x[1]=='+' else 3)    #위치, 방향
    for i in range(3):
        for j in range(3):
            print(color[arr[cube[0][i][j]]], end='')
        print()
