class node:
    def __init__(self, ch, parent = None):
        if parent is not None:
            self.s = parent.s + ch
        else:
            self.s = ''
        self.children = {}
    def make_edge(self, ch):
        if ch not in self.children.keys():
            self.children[ch] = node(ch, self)
            return True
        else:
            return False
    def __repr__(self):
        return self.s
    
s = input()

root = node('')
vertices = [root]
stand = root
for i in range(len(s)):
    word = s[i:]
    for ch in word:
        new = stand.make_edge(ch)
        stand = stand.children[ch]
        if new:
            vertices.append(stand)
    stand = root

print(len(vertices) - 1)