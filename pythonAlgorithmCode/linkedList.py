#https://www.acmicpc.net/problem/1406

from sys import *
setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()
class Node:
    def __init__(self, value=None):
        self.prev = None
        self.nxt = None
        self.value = value
class LL:
    def __init__(self, mkString):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.pointer = self.head
        for i in range(len(mkString)):
            self.add(mkString[i])

    def add(self, value):
        self.temp = Node(value)
        self.pointer.nxt.prev = self.temp
        self.temp.nxt = self.pointer.nxt
        self.pointer.nxt = self.temp
        self.temp.prev = self.pointer
        self.pointer = self.pointer.nxt
    def left(self):
        if self.pointer != self.head:
            self.pointer = self.pointer.prev
    def right(self):
        if self.pointer.nxt != self.tail:
            self.pointer = self.pointer.nxt
    def remove(self):
        if self.pointer != self.head:
            self.pointer.prev.nxt = self.pointer.nxt
            self.pointer.nxt.prev = self.pointer.prev
            self.pointer = self.pointer.prev
    def __str__(self):
        temp = self.pointer
        ans=''
        while temp.prev:
            temp = temp.prev
        while temp.nxt != self.tail:
            temp = temp.nxt
            ans += temp.value
        return ans
a = input()
ll = LL(a)
n = int(input())
for i in range(n):
    inp = list(map(str, input().split()))
    if inp[0] == 'L':
        ll.left()
    elif inp[0] == 'D':
        ll.right()
    elif inp[0] == 'B':
        ll.remove()
    else:
        ll.add(inp[1])
print(ll)
