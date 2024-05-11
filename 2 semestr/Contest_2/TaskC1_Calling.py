def read_graph_as_edges_w():
    n, m, p0 = map(int, input().split())
    p_set = set(map(int, input().split()))
    p = len(p_set)
    graph1 = []
    graph2 = []
    for i in range(m):
        e1 = list(map(int, input().split()))
        e2 = [e1[1], e1[0], e1[2]]
        graph1.append(e1)
        graph1.append(e2)
        if e1[0] not in p_set and e1[1] not in p_set:
            graph2.append(e1)
            graph2.append(e2)
    return graph1, graph2, p_set, n, p


def read_graph_as_neigh_list_w(edge_list):
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict

def prim(graph):
    n = len(graph)
    mst = []
    visited = {}
    min_edge = {}
    s = 0
    for i in graph.keys():
        visited[i] = False
        min_edge[i] = float('inf')
    min_edge[min(list(graph.keys()))] = 0

    for _ in range(n):
        v = -1
        for i in graph.keys():
            if not visited[i] and (v == -1 or min_edge[i] < min_edge[v]):
                v = i
        visited[v] = True
        if min_edge[v] != float('inf'):
            mst.append((v, min_edge[v]))
            s += min_edge[v]

        for edge in graph[v]:
            to, weight = edge
            if not visited[to] and weight < min_edge[to]:
                min_edge[to] = weight

    return mst, s

def main_task():
    edge_list1, edge_list2, p_set, n, p = read_graph_as_edges_w()
    graph = read_graph_as_neigh_list_w(edge_list1)
    if len(graph.keys()) != n:
        return 'impossible'
    graph_p = read_graph_as_neigh_list_w(edge_list2)
    if len(graph_p.keys()) < n - p:
        return 'impossible'
    graph_p_ost, s = prim(graph_p)
    for v in p_set:
        k = 0
        s0 = float('inf')
        for neigh in graph[v]:
            if neigh[0] in p_set:
                k+=1
            else:
                if neigh[1] < s0:
                    s0 = neigh[1]
        if k == len(graph[v]):
            return 'impossible'
        s+=s0
    return s

print(main_task())

