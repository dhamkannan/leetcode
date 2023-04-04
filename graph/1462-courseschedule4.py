numCourses = 3
# prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,5]]
prerequisites = [[1,2],[1,0],[2,0]]
queries = [[1,0],[1,2]]

def checkIfPrerequisite(numCourses, prerequisites, queries):
    adjM = {}
    for i in range(numCourses):
        adjM[i] = set()
    for prereq in prerequisites:
        adjM[prereq[1]].add(prereq[0])
    print(adjM)
    prereqMatrix = {}
    def dfs(course):
        if course in prereqMatrix:
            return prereqMatrix[course]
        prereqMatrix[course] = set()
        for preq in adjM[course]:
            prereqMatrix[course].add(preq)
            prereqMatrix[course].update(dfs(preq))
        return prereqMatrix[course]
    for course in adjM:
        dfs(course)
    res = []
    print(prereqMatrix)
    for query in queries:
        res.append(True if query[0] in prereqMatrix[query[1]] else False)
    return res

print(checkIfPrerequisite(numCourses, prerequisites, queries))