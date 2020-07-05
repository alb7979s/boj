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
        self.rootList=deque()
    def merge(self, x, y):
        xfreq, xkey = x
        yfreq, ykey = y
        #key가 INF이 아니면 리프노드로 생성
        if xkey!=INF: xNode = Node(xfreq, xkey)
        #key가 INF이면 이미 생성된 노드 있음, 찾아옴
        else: xNode = self.find(xfreq, xkey)
        if ykey!=INF: yNode = Node(yfreq, ykey)
        else: yNode = self.find(yfreq, ykey)
        #합친 값으로 부모노드 생성하고 연결
        parent = Node(xfreq+yfreq, INF)
        parent.left = xNode
        parent.right = yNode
        #root 추가
        self.rootList.append(parent)
        self.root = self.rootList[0]
    def find(self, freq, key):   #data == freq
        #합칠때 찾아지면 이제 루트 아님 빼줌
        while self.rootList:
            root = self.rootList.popleft()
            node = self._find(root, freq, key)
            if node is None:
                self.rootList.append(self.rootList.popleft())
            else:
                return node
    def _find(self, node, data, key):
        if node is None or (data == node.data and key == node.key): return node
        if data < node.data: return self._find(node.left, data, key)
        if data > node.data: return self._find(node.right, data, key)
    def findKey(self, data, key):
        return self._findKey(self.root, data, key, '')
    def _findKey(self, node, data, key, res):
        if node is None or data == node.data: return res
        if data < node.data: return self._findKey(node.left, data, key, res+'0')
        if data > node.data: return self._findKey(node.right, data, key, res+'1')
    #잘 만들어졌나 확인
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
    #테이블 생성
    def makeHTTable(self):
        self.intable={}
        self.detable={}
        self._makeHTTable(self.root, '')
    def _makeHTTable(self, node, res):
        if node is None: return
        if node.key != INF:
            self.intable[hs.keyList[node.key]] = res
            self.detable[res] = hs.keyList[node.key]
            return
        self._makeHTTable(node.left, res+'0')
        self._makeHTTable(node.right, res+'1')
    #O(logn)으로 찾는 decoding인데 위에 detable 만들어서 O(1)로 가능, 그래서 만들긴 했지만 사용은 안함
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
if len(pq)==1:     #주어진 자료에 문자가 하나밖에 없을때 예외처리
    heappush(pq,[INF, INF])
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
    res+=ht.intable[a[i]]
print('인코딩:',res)
#디코딩
ans=''
temp=''
for i in range(len(res)):
    temp += res[i]
    try:
        ans += ht.detable[temp]
        temp=''
    except:
        pass
print('디코딩:',ans)
