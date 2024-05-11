def read_graph_as_neigh_matrix_w():
    r, c, n = map(int, input().split())
    cuts_list = list(map(int, input().split()))
    cuts = set()
    for i in range(len(cuts_list)):
        if i%2 == 1:
            cuts.add((cuts_list[i-1], cuts_list[i]))
    
    res_matrix = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if ((i, j) not in cuts):
                res_matrix[i][j] = 1
    return res_matrix

def DFS(v, visited, match, graph):
    for u in range(len(graph[v])):
        if graph[v][u] == 1 and not visited[u]:
            visited[u] = True
            if match[u] == -1 or DFS(match[u], visited, match, graph):
                match[u] = v
                return True
    return False

def kuhn_algorithm(graph):
    m, n = len(graph), len(graph[0])
    match = [-1]*n
    result = 0

    for i in range(m):
        visited = [False]*n
        if DFS(i, visited, match, graph):
            result += 1
    
    return match 


def main_task():
    graph = read_graph_as_neigh_matrix_w()
    graph_pair = kuhn_algorithm(graph)
    gr = [i for i in graph_pair if i >= 0]
    answer = len(gr)
    return answer

t = int(input())
for i in range(t):
    print(main_task())