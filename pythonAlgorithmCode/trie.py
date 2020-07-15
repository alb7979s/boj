class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
class Trie:
    def __init__(self):
        self.root = Node(None)
    def insert(self, string):
        cur_node = self.root
        for char in string:
            if char not in cur_node.children:   #?? 시간 ㄱㅊ?
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
        cur_node.data = string  #마지막 스트링 저장 공간 ㄱㅊ?
    def search(self, string):
        cur_node = self.root
        for char in string:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
            else:
                return False
        if cur_node.data != None: return True
    def starts_with(self, prefix):
        cur_node = self.root
        res = []
        subtrie = None
        for char in prefix:
            if char in cur_node.children:
                cur_node = cur_node.children[char]
                subtrie = cur_node
            else:
                return None
        v = list(subtrie.children.values())
        while v:
            cur = v.pop()
            if cur.data != None:
                res.append(cur.data)
            v += list(cur.children.values())
        return res
t = Trie()
words = ["romane", "romanus", "romulus", "ruben", 'rubens', 'ruber', 'rubicon', 'ruler']
for word in words:
    t.insert(word)

print(t.search("romulus"))
print(t.search("ruler"))
print(t.search("rulere"))
print(t.search("romunus"))
print(t.starts_with("ro"))
print(t.starts_with("rube"))
#출처 https://gist.github.com/osori/d0200b9bb7665d6a69da61b431e4077f
