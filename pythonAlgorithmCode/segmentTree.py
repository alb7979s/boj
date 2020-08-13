#2042 구간합 
from sys import*
from math import*
input=stdin.readline
setrecursionlimit(10**6)
class SegmentTree:
    def __init__(self, n):
        h = int(ceil(log2(n)))
        self.tree = [0] * (1<<(h+1))
        self._init(1, 0, n-1)
    def _init(self, node, s, e):
        if s==e:
            self.tree[node] = a[s]
            return self.tree[node]
        m = (s+e)//2
        self.tree[node] = self._init(node*2, s, m) + self._init(node*2+1, m+1, e)
        return self.tree[node]
    def update(self, node, s, e, idx, diff):
        if not s<=idx<=e: return
        self.tree[node] += diff
        if s!=e:
            m = (s+e)//2
            self.update(node*2, s, m, idx, diff)
            self.update(node*2+1, m+1, e, idx, diff)
    def cal(self, node, s, e, l, r):
        if l>e or r<s: return 0
        if l<=s and e<=r: return self.tree[node]
        m = (s+e)//2
        return self.cal(node*2, s, m, l, r) + self.cal(node*2+1, m+1, e, l, r)
n, m, k = map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
st = SegmentTree(n)
for i in range(m+k):
    x, y, z = map(int,input().split())
    y-=1
    if x==1:
        st.update(1, 0, n-1, y, z-a[y])
        a[y] = z
    else:
        z-=1
        print(st.cal(1, 0, n-1, y, z))
