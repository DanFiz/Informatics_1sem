
from collections import deque
from copy import deepcopy

def read_graph_as_neigh_matrix_w():
    n = int(input())
    res_matrix = []
    for i in range(n):
        line = input()
        line_list = []
        for j in line:
            line_list.append(int(j))
        res_matrix.append(line_list)
    return res_matrix, n

def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(s)
    visited[s] = True
    
    while queue:
        u = queue.popleft()
        
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                
    return visited[t]

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs(graph, source, sink, parent):
        path_flow = float('inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
            
        max_flow += path_flow
        
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
            
    return max_flow


def main_task():
    graph, n = read_graph_as_neigh_matrix_w()
    answer = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            gr = deepcopy(graph)
            a = edmonds_karp(gr, i, j)
            if a < answer:
                answer = a
    return answer

t = int(input())
for i in range(t):
    print(main_task())

