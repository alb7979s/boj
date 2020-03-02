from sys import*
input = stdin.readline

def solve(pos, res):
    ans = 0
    if pos > n: return 0
    if pos == n: return res
    ans = max(ans, solve(pos+a[pos][0], res+a[pos][1]), solve(pos+1, res))
    return ans

n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))    #[0]날짜, [1]금액
print(solve(0,0))
