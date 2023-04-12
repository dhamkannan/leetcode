# edges = [[1,2],[1,3],[2,3]]
# edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# edges = [[1,5],[3,4],[3,5],[4,5],[2,4]]
# edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
edges = [[1,5],[2,4],[3,4],[1,3],[3,5]]

def findRedundantConnection(edges):
    par = [ i for i in range(len(edges)+1)]
    rank = [1 for i in range(len(edges)+1)]
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
            return False
        elif rank[p1] >= rank[p2]:
            par[p2] = p1
            par[node2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            par[node1] = p2
            rank[p2] += rank[p1]
        return True
    
    for edge in edges:
        if not union(edge[0], edge[1]):
            return edge
    
print(findRedundantConnection(edges))