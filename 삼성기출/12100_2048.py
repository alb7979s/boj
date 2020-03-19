from sys import*
from collections import*
input = stdin.readline
def move(d):
    global res
    if d==0 or d==3:    #U or L
        for i in range(n):
            st=[]; idx=0
            for j in range(n):
                val = a[j][i] if d==0 else a[i][j]
                if val == 0: continue
                try:    #비교할 대상 있는 경우
                    if st[idx] == val:
                        st[idx] *= 2
                        res = max(res, st[idx])
                    else:
                        st.append(val)
                    idx += 1
                except: #idx 없는 경우(추가 해야하는 경우)
                    st.append(val)
            for j in range(len(st)):
                if d==0: a[j][i]=st[j]
                else: a[i][j]=st[j]
            for j in range(len(st),n):
                if d==0: a[j][i]=0
                else: a[i][j]=0
    elif d==1 or d==2:    #R or D
        for i in range(n):
            st=[]; idx=0
            for j in range(n-1, -1, -1):
                val = a[j][i] if d==2 else a[i][j]
                if val ==0: continue
                try:
                    if st[idx] == val:
                        st[idx] *= 2
                        res=max(res, st[idx])
                    else:
                        st.append(val)
                    idx += 1
                except:
                    st.append(val)
            for j in range(len(st)):
                if d==2: a[-(j+1)][i]=st[j]
                else: a[i][-(j+1)]=st[j]
            for j in range(len(st), n):
                if d==2: a[-(j+1)][i]=0
                else: a[i][-(j+1)]=0
def solve(cnt):
    global a
    if cnt == 5: return
    b=[x[:] for x in a]
    for i in range(4):
        move(i)
        solve(cnt+1)
        a=[x[:] for x in b]
    return
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
res=0
for i in range(n):
    res=max(res, max(a[i]))
solve(0)
print(res)
