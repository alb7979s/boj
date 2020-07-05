#허프만코드 이진트리로 구현
#200725
from heapq import*
from collections import*
from sys import*
input = lambda:stdin.readline().strip()
INF=1e9
class hash:
    def __init__(self):
        self.idx=0
        self.dic={}
        self.keyList=[]
    def stoi(self, string):
        try:
            return self.dic[string]
        except:
            self.dic[string] = self.idx
            self.keyList.append(string)
            self.idx+=1
            return self.dic[string]
    def itos(self, index):
        return self.keyList[index]
class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.left = self.right = None
class HuffmanTree:
    def __init__(self):
        self.root = None
    def merge(self, x, y):
        xfreq, xkey = x
        yfreq, ykey = y
        #key가 INF이 아니면 리프노드로 생성
        if xkey!=INF: xNode = Node(xfreq, xkey)
        #key가 INF이면 이미 생성된 노드 있음, 찾아옴
        else: xNode = self.find(xfreq)
        if ykey!=INF: yNode = Node(yfreq, ykey)
        else: yNode = self.find(yfreq)
        #합친 값으로 부모노드 생성하고 연결
        parent = Node(xfreq+yfreq, INF)
        parent.left = xNode
        parent.right = yNode
        #root 갱신
        self.root=parent
    def find(self, freq):   #data == freq
        return self._find(self.root, freq)
    def _find(self, node, data):
        if node is None or data == node.data: return node
        if data < node.data: return self._find(node.left, data)
        if data > node.data: return self._find(node.right, data)
    def findKey(self, data, key):
        return self._findKey(self.root, data, key, '')
    def _findKey(self, node, data, key, res):
        if node is None or data == node.data: return res
        if data < node.data: return self._findKey(node.left, data, key, res+'0')
        if data > node.data: return self._findKey(node.right, data, key, res+'1')
    def levelorder(self):
        self._levelorder(self.root)
    def _levelorder(self, node):
        q=deque()
        q.append(node)
        while q:
            node = q.popleft()
            if node is None: continue
            print(node.data, node.key)
            q.append(node.left)
            q.append(node.right)
    def makeHTTable(self):
        self.table=['' for _ in range(maxLen)]
        self._makeHTTable(self.root, '')
    def _makeHTTable(self, node, res):
        if node is None: return
        if node.key != INF: self.table[node.key] = res
        self._makeHTTable(node.left, res+'0')
        self._makeHTTable(node.right, res+'1')
    def decoding(self, string):
        return self._decoding(self.root, string, 0)
    def _decoding(self, node, string, pos):
        if node.key != INF: return node.key
        if pos == len(string): return INF
        if string[pos] == '0': return self._decoding(node.left, string, pos+1)
        if string[pos] == '1': return self._decoding(node.right, string, pos+1)

a=input()
hs=hash()
for i in range(len(a)):
    hs.stoi(a[i])
maxLen = hs.idx
cnt = [[0, i]for i in range(maxLen)]    #[0]개수, [1]idx
for i in range(len(a)):                 #카운팅
    cnt[hs.dic[a[i]]][0] += 1
pq = []
for i in range(maxLen):
    heappush(pq, cnt[i])
ht = HuffmanTree()
while len(pq)>1:   #하나 남을 때까지
    x = heappop(pq)
    y = heappop(pq)
    ht.merge(x, y)
    heappush(pq, [x[0]+y[0], INF])
#ht.levelorder()
ht.makeHTTable()
#for i in range(maxLen):
#    print(hs.keyList[i], ht.table[i])
#인코딩
res=''
for i in range(len(a)):
    res+=ht.table[hs.dic[a[i]]]
print(res)
#디코딩
ans=''
temp=''
for i in range(len(res)):
    temp += res[i]
    dt = ht.decoding(temp)
    if dt!=INF:
        ans += hs.keyList[dt]
        temp=''
print(ans)
