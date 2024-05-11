def read_graph_as_edges_w():
    n0, a0, b0, c0, d = map(float, input().split())
    n = int(n0)
    a = int(a0)
    b = int(b0)
    c = int(c0)
    m = int(input())
    graph = []
    for i in range(m):
        e1 = list(map(float, input().split()))
        e2 = [e1[1], e1[0], e1[2]]
        graph.append(e1)
        graph.append(e2)
    return graph, a, b, c ,d, n


def read_graph_as_neigh_list_w(edge_list, n):
    graph_dict = {}
    for v in range(1, n + 1):
        graph_dict[v] = frozenset()
    for edge in edge_list:
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1],edge[2])])
    return graph_dict

def Dijkstra_compute_min_distances(graph, v):
    distances = {}
    visited = []
    for key in graph.keys():
        distances[key] = float('infinity')
    distances[v] = 0
    visited.append((0, v))
    while visited:
        visited.sort()
        current_node = visited.pop(0)
        cur_dist, cur_node = current_node

        if cur_dist > distances[cur_node]:
            continue

        for neighbor in graph[current_node[1]]:
            if (distances[current_node[1]] + neighbor[1]) < distances[neighbor[0]]:
                distances[neighbor[0]] = (distances[current_node[1]] + neighbor[1])
                vis = neighbor[::-1]
                visited.append(tuple(vis))

    return distances

import heapq

def dijkstra(graph, start):
    distances = {}
    for key in graph.keys():
        distances[key] = float('infinity')
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        cur_dist, cur_node = heapq.heappop(pq)

        if cur_dist > distances[cur_node]:
            continue

        for neighbor, weight in graph[cur_node]:
            distance = cur_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def main_task():
    edge_list, a, b, c ,d, n = read_graph_as_edges_w()
    graph = read_graph_as_neigh_list_w(edge_list, n)
    distances_a = Dijkstra_compute_min_distances(graph, a)
    a_c = distances_a[c]
    a_b = distances_a[b]
    if a_c == float('inf') or a_b == float('inf'):
        return -1
    else:
        distances_b = Dijkstra_compute_min_distances(graph, b)
        b_c = distances_b[c]
        return (a_b + b_c - a_c)*d

print(main_task())

