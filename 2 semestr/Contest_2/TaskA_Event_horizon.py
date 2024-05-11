def read_graph_as_edges_w():
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph


def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges_w()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict

def task_array_by_Dijkstra(graph):
    distances = {}
    visited = []
    flag = True
    k = 0
    n = len(list(graph.keys()))
    edge_max = n*(n-1)
    v = min(list(graph.keys()))
    for key in graph.keys():
        distances[key] = float('infinity')
    distances[v] = 0
    visited.append([0, v])

    while visited and k < (n+1)+edge_max:
        k += 1
        visited.sort()
        current_node = visited.pop(0)
        for neighbor in graph[current_node[1]]:
                if (distances[current_node[1]] + neighbor[1]) < distances[neighbor[0]]:
                    if (k > (n-1)) and (distances[neighbor[0]] != float('infinity')):
                        flag = False
                        return flag
                    distances[neighbor[0]] = (distances[current_node[1]] + neighbor[1])
                    visited.append(neighbor[::-1])

    return flag

def BellmanFord(V, graph):
    dist = {}
    for i in graph.keys():
        dist[i] = float('inf')
    dist[V] = 0
    m = len(dist)

    for j in range(m - 1):
        for i in graph.keys():
            for neigh in graph[i]:
                u = i
                v = neigh[0]
                weight = neigh[1]
                if (dist[u] != float('inf') and dist[u] + weight < dist[v]):
                    dist[v] = dist[u] + weight
 
    for i in graph.keys():
        for neigh in graph[i]:
            u = i
            v = neigh[0]
            weight = neigh[1]
            if (dist[u] != float('inf') and dist[u] + weight < dist[v]):
                return True
 
    return False


graph = read_graph_as_neigh_list_w()

result = BellmanFord(0, graph)

if result == True:
     print('yes')
else:
     print('no')