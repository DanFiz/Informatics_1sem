
def read_graph_as_edges(n):
    try:
        graph = [list(map(int, input().split())) for i in range(n)]
        return graph
    except ValueError:
        print('Вы ввели не то количество ребер графа, что указали')


def read_graph_as_neigh_matrix(edge_list, n):

    V_num = n

    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = 1
    return res_matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)



def task3():
    n, m = map(int, input().split())
    if m != n*(n-1)/2:
        result = 'no'
        return result
    result = 'yes'
    graph = read_graph_as_edges(m)
    matrix = read_graph_as_neigh_matrix(graph, n)
    for i in range(n):
        for j in range(n):
            if i != j and (matrix[i][j] + matrix[j][i] != 1):
                result = 'no'
                return result
            if matrix[j][j] != 0:
                result = 'no'
                return result

    return result



print(task3())