#Work In Progress# Leet code 13/17 Passed
import heapq
from collections import defaultdict

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]


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
    group2 = []
    m2 = m
    for g in group:
        if g == -1:
            group2.append(m2)
            m2 += 1
        else:
            group2.append(g) 
    groupsMap = defaultdict(list)
    # [0,0,2,1,0]
    # [[3],[],[],[],[1,3,2]]
    for k, groups in enumerate(group2):
        groupsMap[groups].append(k)
    localItems = [[] for _ in range(n)]
    groupItems = [[] for _ in range(n)]
    for i, items in enumerate(beforeItems):
        currgroup = group2[i]
        for item in items:
            if group2[item] == currgroup:
                localItems[i].append(item)
            else:
                for x in groupsMap[group2[i]]:
                    # groupItems[x].append(item)
                    groupItems[x] += groupsMap[group2[item]]
    print('group2', group2)
    print('gmap', groupsMap)
    print('litems', localItems)
    print('gitems', groupItems)
    visit = set()
    path = set()
    visit2 = set()
    path2 = set()
    res = []
    def dfs2(node):
        if node in path2:
            return 'no'
        if node in visit2:
            return
        visit2.add(node)
        path2.add(node)
        for nnode in localItems[node]:
            if dfs2(nnode) == 'no':
                return 'no'
        res.append(node)
        path2.remove(node)

    def dfs(groupNode):
        if groupNode in path:
            return 'no'
        
        if groupNode in visit:
            return
        visit.add(groupNode)
        path.add(groupNode)
        for ngroup in groupItems[groupNode]:
            if dfs(ngroup) == 'no':
                return 'no'
        if dfs2(groupNode) == 'no':
            return 'no'
        path.remove(groupNode)
    for item in range(n):
        if dfs(item) == 'no':
            return []
    return res




print(sortItems(n,m,group,beforeItems))