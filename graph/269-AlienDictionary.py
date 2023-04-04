words = ["wrt", "wrf", "er", "ett", "rftt"]

def leetcode():
    adjMap = {}

    for word in words:
        for c in word:
            adjMap[c] = set()

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                adjMap[w1[j]].add(w2[j])
    print(adjMap)
    visited = set()
    path = set()
    res = []

    def dfs(node):
        if node in path:
            return 'loop'

        if node in visited:
            return

        visited.add(node)
        path.add(node)

        for nnode in adjMap[node]:
            if dfs(nnode) == 'loop':
                return 'loop'

        path.remove(node)
        res.append(node)

    for node in adjMap:
        if dfs(node) == 'loop':
            return ""

    res.reverse()
    return "".join(res)

print(leetcode())