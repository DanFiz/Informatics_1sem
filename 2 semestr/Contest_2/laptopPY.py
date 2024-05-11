from math import sqrt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def prim_mst(self):
        parent = [i for i in range(self.V)]  
        rank = [0] * self.V  
        mst_edges = []  

        
        self.graph.sort(key=lambda x: x[2])
        mst = []
        i = 0
        while len(mst_edges) < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                mst_edges.append((u, v))
                mst.append(w)
                self.union(parent, rank, x, y)

        return mst


n = int(input())

for k in range(n):
    s, p = map(int, input().split())
    vishky = Graph(p)
    coords = []
    for i in range(p):
        x, y = map(int, input().split())
        coords.append((x, y))
    for i in range(p):
        for j in range(i+1, p):
            vishky.addEdge(
                i, j, (coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2)
    answer = vishky.prim_mst()
    answer.sort()
    print("{:.2f}".format(sqrt(answer[p - s - 1])))