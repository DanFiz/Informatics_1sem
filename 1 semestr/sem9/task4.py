class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None
class DoublyLinkedList:
    def __init__(self):
        self.start_node = None
    def __len__(self):
        if self.start_node==None:
            return 0
        else:
            n = self.start_node
            i=1
            while n.nref is not None:
                n = n.nref
                i+=1
            return i

    def add(self, data, index=None):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            if index==None:
                n = self.start_node
                while n.nref is not None:
                    n = n.nref
                new_node = Node(data)
                n.nref = new_node
                new_node.pref = n
            elif index>=len(self):
                print('The index exceeds the length of the list')
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
    def value(self,index=None):
        if self.start_node is None:
            print("List is empty")
            return ''
        elif index == None:
            return self.start_node.item
        elif index >= len(self):
            print('The index exceeds the length of the list')
        else:
            lastnode = self.start_node
            nodeindex = 0
            while nodeindex <= index:
                if nodeindex == index:
                    break
                nodeindex = nodeindex + 1
                lastnode = lastnode.nref
            return lastnode.item
    def delit(self,index=None):
        if self.start_node is None:
            print("List is empty")
        else:
            if index==None:
                n = self.start_node
                while n.nref is not None:
                    n = n.nref
                if n.pref is not None:
                    n.pref.nref = None
                else:
                    self.start_node=None
            elif index>=len(self):
                print('The index exceeds the length of the list')
            else:
                lastnode=self.start_node
                nodeindex=0
                while nodeindex <= index:
                    if nodeindex == index:
                        n = lastnode
                        break
                    nodeindex = nodeindex + 1
                    lastnode = lastnode.nref
                if n.pref is not None and n.nref is not None:
                    n.pref.nref = n.nref
                    n.nref.pref=n.pref
                elif n.pref is not None:
                    n.pref.nref=None
                elif n.nref is not None:
                    n.nref.pref=None
                else:
                    self.start_node=None
    def print(self):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref
print('Введите длину списка')
n=int(input())
list=DoublyLinkedList()
print('Введите элементы списка через enter')
for i in range(n):
    list.add(input())
list.add(100,2)
list.print()
print(f'Количество элементов в списке: {len(list)}')
print(f'Значение у элемента с индексом 2: {list.value(2)}')
list.delit(2)
list.print()