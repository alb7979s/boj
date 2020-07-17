#https://www.acmicpc.net/problem/5052
from sys import*
setrecursionlimit(10**6)
input = lambda:stdin.readline().strip()
class Node:
    def __init__(self):
        self.end = False
        self.child = {}

class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, string):
        node = self.root
        for i, char in enumerate(string):
            if i == len(string)-1:
                if char in node.child: return False
            if char not in node.child: node.child[char] = Node()
            node = node.child[char]
            if node.end: return False
        node.end = True
        return True
for tc in range(int(input())):
    trie = Trie()
    n = int(input())
    YES=True
    for i in range(n):
        a=input()
        if not YES:continue
        if not trie.insert(a):
            YES=False
    if YES: print("YES")
    else:print("NO")

