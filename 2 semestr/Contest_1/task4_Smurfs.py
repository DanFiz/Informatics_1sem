'''def read_graph_as_edges():
    try:
        n = int(input())
        graph = [list(map(int, input().split())) for i in range(n)]
        # for i in range(n):
        #     graph.append(list(map(int, input().split())))
        return  graph
    except ValueError:
        print('Вы ввели не то количество ребер графа, что указали')'''
def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
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
    return graph_dict


def has_cycle(graph, v, visited=[]):
    result = False
    for neigh in graph[v]:
        if neigh in visited:
            result = True
            return result

        visited.append(v)

        if result == False:
            result = has_cycle(graph, neigh, visited)
            visited = []
    return result

def read_graph_as_edges():
    n = int(input())
    graph = [0 for i in range(n)]
    for i in range(n):
        s_l,sign, s_r = input().split(' ')
        if sign == '>':
            graph[i] = [s_l, s_r]
        else:
            graph[i] = [s_r, s_l]
    return graph
def task4(graph):
    answer = 'possible'
    for v in graph.keys():
        result = has_cycle(graph, v, visited = [])
        if result == True:
            answer = 'impossible'
            return answer
    return answer
graph = read_graph_as_neigh_list()
print(task4(graph))



