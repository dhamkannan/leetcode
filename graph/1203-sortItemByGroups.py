#Work In Progress#
import heapq

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]

# n = 10
# m = 4
# group = [0,1,1,2,3,-1,0,0,0,1]
# beforeItems = [[2,5],[3,5,4,6,8,7,2],[7],[],[],[],[],[],[],[]]

# n = 8
# m = 2
# group = [-1,-1,1,0,0,1,0,-1]
# beforeItems = [[],[6],[5],[6],[3],[],[4],[]]

# n = 5
# m = 5
# group = [2,0,-1,3,0]
# beforeItems = [[2,1,3],[2,4],[],[],[]]

def sortItems1(n,m,group,beforeItems):
    maxHeap = []
    for i in range(n):
        heapq.heappush(maxHeap,(-1*group[i], i))
    print(maxHeap)
    res = []
    order = []
    visit = set()
    path = set()
    order = set()
    def dfs(node):
        if node in path:
            return 'no'
        
        if node in visit:
            return
        visit.add(node)
        path.add(node)
        for nnode in beforeItems[node]:
            if dfs(nnode) == 'no':
                return 'no'
        
        if not order:
            order.append(group[node])
        elif group[node] == -1 or group[node] == order[-1]:
            pass
        elif group[node] in order:
                return 'no'
        else:
            order.append(group[node])
        res.append(node)
        path.remove(node)
    while maxHeap:
        j, node = heapq.heappop(maxHeap)
        if dfs(node) == 'no':
            return []
    return res

def sortItems(n,m,group,beforeItems):
    maxHeap = []
    for i in range(n):
        heapq.heappush(maxHeap,(-1*group[i], i))
    print(maxHeap)
    res = [[] for _ in range(m+1)]
    order = []
    visit = set()
    path = set()
    def dfs(node):
        if node in path:
            return 'no'
        
        if node in visit:
            return
        visit.add(node)
        path.add(node)
        for nnode in beforeItems[node]:
            if dfs(nnode) == 'no':
                return 'no'
        
        if not order:
            order.append(group[node])
        elif group[node] == -1 or group[node] == order[-1]:
            pass
        elif group[node] in order:
                return 'no'
        else:
            order.append(group[node])
        res[group[node]].append(node)
        path.remove(node)
    while maxHeap:
        j, node = heapq.heappop(maxHeap)
        if dfs(node) == 'no':
            return []
    return res



print(sortItems(n,m,group,beforeItems))