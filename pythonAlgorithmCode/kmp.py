#https://www.acmicpc.net/problem/1786
#s짚더미, p바늘
def getPi(p):
    m = len(p)
    pi = [0] * (m+1)
    j = 0
    for i in range(1, m):
        while j>0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j+=1
            pi[i] = j
    return pi
def kmp(s, p):
    n = len(s); m = len(p)
    j = 0
    ans = []
    for i in range(n):
        while j>0 and s[i] != p[j]:
            j = pi[j-1]
        if s[i] == p[j]:
            if j == m-1:
                ans.append(i-m+1)
                j = pi[j]
            else:j+=1
    return ans
s = input()
p = input()
pi = getPi(p)
ans = kmp(s, p)
print(len(ans))
for x in ans:
    print(x+1, end=' ')
