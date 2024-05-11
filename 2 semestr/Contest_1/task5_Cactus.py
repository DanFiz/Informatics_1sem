'''def read_graph_as_edges_in():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    return graph'''





'''def has_cycle(graph, v, visited = [], st = set(), i = 0):
    result = False
    q = 1
    for neigh_c in graph[v]:
        neigh = neigh_c[0]
        if neigh in visited:
            print(neigh)
            if neigh_c[1] == 0:
                print(0)
                st.add(neigh)
                graph[v] = set(graph[v])
                graph[v].remove(neigh_c)
                graph[v] = frozenset(graph[v]) | frozenset({(neigh_c[0], 1)})
                q0 = len(st)
            elif neigh_c[1] == 1:
                print(1)
                i+=1
                q0 = len(st)
                st.add(neigh)
            if len(st)>q0:
                return True, 0
            while i<len(st):
                result, q = has_cycle(graph, neigh, visited, st, i)
                if result == True:
                    return result, q

            graph[v] = set(graph[v])
            graph[v].remove(neigh_c)
            graph[v] = frozenset(graph[v])
            q = q0 + 1

            visited = []
            result = True
            return result, q

        visited.append(v)

        if result == False:
            result, q = has_cycle(graph, neigh, visited, st, i)
            print(result, q)
            if result == True:
                return result, q
            visited = []
    return result, q

def read_graph_as_neigh_list_in():
    edge_list, first_list, n = read_graph_as_edges()
    e = len(edge_list)
    graph_dict = {}
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], 0)])
    return graph_dict, first_list, n, e'''

def read_graph_as_neigh_list():
    edge_list, first_list, n = read_graph_as_edges()
    e = len(edge_list)
    graph_dict = {} #dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    #V_num = len(vertex_set)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]]= graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict, first_list, n, e


def read_graph_as_edges():
    n, m = map(int, input().split())
    paths = [list(map(int, input().split())) for i in range(m)]
    edge_list = []
    first_list = []
    for path in paths:
        path.pop(0)
        v = path.pop(0)
        first_list.append(v)
        while path:
            neigh = path.pop(0)
            edge_list.append([v, neigh])
            edge_list.append([neigh, v])
            v = neigh
    return edge_list, first_list, n





def has_cycle(graph, v, visited=[], st = set(), q_list = [], last_neigh = None):
    result = False
    for neigh in graph[v]:
        if neigh != last_neigh:
            if neigh in visited:
                visited.append(v)
                if neigh not in st:
                    ind = visited.index(neigh)
                    st_lt = set(visited[ind:])
                    if len(st_lt) < 3:
                        continue
                    q_list.append(len(st_lt) + 1)
                    for elem in st_lt:
                        if elem not in st:
                            st.add(elem)
                        else:
                            q_list.append(0)
                    graph[v] = set(graph[v])
                    graph[v].remove(neigh)
                    graph[v] = frozenset(graph[v])
                    graph[neigh] = set(graph[neigh])
                    graph[neigh].remove(v)
                    graph[neigh] = frozenset(graph[neigh])

                else:
                    q_list.append(0)
                result = True
                return result

            visited.append(v)

            if result == False:
                result = has_cycle(graph, neigh, visited, st, q_list, last_neigh = v)
                visited = []
    return result



def task5_Cactus():
    graph, first_list, n, e = read_graph_as_neigh_list()
    key = len(graph.keys())
    if key != n or e > 3*(n-1):
        return 0
    st_lt = set()
    q_lt = []
    for v in graph.keys():
        if v not in st_lt:
            has_cycle(graph, v, visited = [], st = st_lt, q_list = q_lt)
            if 0 in q_lt:
                return 0
    if q_lt == []:
        return 1
    else:
        q = 1
        for q0 in q_lt:
            q *= q0
        return q


print(task5_Cactus())




