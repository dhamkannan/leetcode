numCourses = 2
# prerequisites = [[1,0],[2,0],[3,1],[3,2],[4,5]]
prerequisites = [[1,0],[0,1]]

def canFinish(numCourses, prerequisites):
    adjM = {}
    for i in range(numCourses):
        adjM[i] = set()
    for prereq in prerequisites:
        adjM[prereq[0]].add(prereq[1])
    print(adjM)
    res = []
    visit = set()
    path = set()
    def dfs(course):
        if course in path:
            return 'loop'
        if course in visit:
            return
        visit.add(course)
        path.add(course)
        for preq in adjM[course]:
            if dfs(preq) == 'loop':
                return 'loop'
        path.remove(course)
        res.append(course)
    for course in adjM:
        if dfs(course) == 'loop':
            return False
            break
    print(res)
    return True if len(res) == numCourses else False

print(canFinish(numCourses, prerequisites))