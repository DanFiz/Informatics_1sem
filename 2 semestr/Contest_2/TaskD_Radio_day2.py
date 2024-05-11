
class Kruskal:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        self.vertices = vertices

    def make_set(self, vertex):
        self.parent[vertex] = vertex
        self.rank[vertex] = 0

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_u] = root_v
                if self.rank[root_u] == self.rank[root_v]: self.rank[root_v] += 1

    def kruskal(self, edges):
        min_spanning_tree = []
        for vertex in self.vertices:
            self.make_set(vertex)

        sorted_edges = sorted(edges, key=lambda edge: edge[2])

        for edge in sorted_edges:
            u, v, weight = edge
            if self.find(u) != self.find(v):
                self.union(u, v)
                min_spanning_tree.append((u, v, weight))

        return min_spanning_tree


def main_task():
    s, p = map(int, input().split())
    coord = []
    vertices = []
    edge_list = []
    for i in range(p):
        x, y =  map(int, input().split())
        coord.append((x,y))
        vertices.append(i)
        for j in range(i):
            w = (x - coord[j][0]) ** 2 + (y - coord[j][1]) ** 2
            edge_list.append((j, i, w))
    kruskal = Kruskal(vertices)
    graph_ost = kruskal.kruskal(edge_list)
    m = graph_ost[-s][-1]
    st = "{0:.2f}".format(m**0.5)
    return st
n = int(input())
for i in range(n):
    print(main_task())

