def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1
def kruskal(edges, num_vertices):
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(num_vertices)]
    rank = [0] * num_vertices
    mst = []
    for edge in edges:
        u, v, weight = edge
        u_root = find(parent, u)
        v_root = find(parent, v)
        if u_root != v_root:
            mst.append(edge)
            union(parent, rank, u_root, v_root)
    return mst

def find_min_edge(components, edges):
    min_edge = None
    min_weight = float('inf')
    
    for edge in edges:
        u, v, weight = edge
        if components[u] != components[v] and weight < min_weight:
            min_edge = edge
            min_weight = weight
            
    return min_edge

def boruvka(edges, num_vertices):
    ostd = []
    components = [-1] * num_vertices
    num_components = num_vertices
    
    while num_components > 1:
        cheapest_edges = [None] * num_vertices
        
        for edge in edges:
            u, v, weight = edge
            cu = components[u]
            cv = components[v]
            
            if cu == cv:
                continue
                
            if cheapest_edges[cu] is None or cheapest_edges[cu][2] > weight:
                cheapest_edges[cu] = edge
                
            if cheapest_edges[cv] is None or cheapest_edges[cv][2] > weight:
                cheapest_edges[cv] = edge
                
        for edge in cheapest_edges:
            if edge is not None:
                u, v, _ = edge
                cu = components[u]
                cv = components[v]
                
                if cu != cv:
                    ostd.append(edge)
                    
                    for i in range(num_vertices):
                        if components[i] == cv:
                            components[i] = cu
                            
                    num_components -= 1
                    
    return ostd

def main_task():
    s, p = map(int, input().split())
    coord = []
    for i in range(p):
        x, y =  map(int, input().split())
        coord.append((x,y))
    coord.sort()
    edge_list = []
    for i in range(p):
        for j in range(i+1, p):
            w = (coord[i][0] - coord[j][0]) ** 2 + (coord[i][1] - coord[j][1]) ** 2
            edge_list.append((i, j, w))
    graph_ost = boruvka(edge_list, p)
    m = graph_ost[-s][-1]
    st = "{0:.2f}".format(m**0.5)
    return st
n = int(input())
for i in range(n):
    print(main_task())

