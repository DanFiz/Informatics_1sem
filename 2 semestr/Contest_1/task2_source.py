def read_graph_as_edges():
    try:
        n = int(input())
        graph = [list(map(int, input().split())) for i in range(n)]
        # for i in range(n):
        #     graph.append(list(map(int, input().split())))
        return  graph
    except ValueError:
        print('Вы ввели не то количество ребер графа, что указали')
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

def topologicalSortUtil_Stack(graph,v0,stack, k):
    stack1 = []
    stack2 = []
    stack1.append(v0)
    while stack1:
        v = stack1.pop()
        if (graph[v] == frozenset()) and (v not in stack2):
            stack.append(v)
        else:
            for neigh in graph[v]:
                if (neigh not in stack) and (neigh not in stack2):
                    stack2.append(neigh)
                    stack1.append(neigh)
    while stack2:
        stack.insert(0,stack2.pop(-1))
    if v0 not in stack:
        k += 1
        stack.insert(0, v0)
    return k


def Topological_Sort_Stack(graph):
    stack =[]
    k = 0
    for i in graph.keys():
        if i not in stack:
            k = topologicalSortUtil_Stack(graph,i, stack, k)
    return k
graph = read_graph_as_neigh_list()
print(Topological_Sort_Stack(graph))


