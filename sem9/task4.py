class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def add(self, data, index=None):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            n = self.start_node
            if index==None:
                n = self.start_node
                while n.nref is not None:
                    n = n.nref
                new_node = Node(data)
                n.nref = new_node
                new_node.pref = n
            else:
                lastnode=self.start_node
                nodeindex=0
                while nodeindex <= index:
                    if nodeindex == index:
                        n = lastnode
                        break
                    nodeindex = nodeindex + 1
                    lastnode = lastnode.nref
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node
    def print(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref
n=int(input())
list=DoublyLinkedList()
for i in range(n):
    list.add(input())
list.add(100,3)
list.print()