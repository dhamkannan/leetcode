n = 5
edges = [[0,1],[1,2],[3,4],[1,3],[2,3]]

def getConnectedComponents(n, edges):
    par = [ i for i in range(n)]
    rank = [1 for i in range(n)]
    # print(par, rank)

    def find(node):
        p = par[node]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p
    
    def union(node1, node2):
        p1, p2 = find(node1), find(node2)
        if p1 == p2:
            return 0
        elif rank[p1] >= rank[p2]:
            par[p2] = p1
            par[node2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            par[node1] = p2
            rank[p2] += rank[p1]
        return 1
    
    res = n

    for edge in edges:
        res -= union(edge[0],edge[1])
    return res

print(getConnectedComponents(n, edges))
    