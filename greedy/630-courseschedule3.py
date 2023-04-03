import heapq
courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]

def scheduleCourse(courses):
    courses.sort(key=lambda x:(x[1],x[0]))

    daysUsed = 0
    maxHeap = []

    for course in courses:
        dur, daysLeft = course[0], course[1]
        if dur + daysUsed <= daysLeft:
            heapq.heappush(maxHeap, -1*dur)
            daysUsed += dur
        elif maxHeap and (dur < maxHeap[0] * -1):
            daysUsed -= (heapq.heappop(maxHeap)*-1)
            heapq.heappush(maxHeap, -1*dur)
            daysUsed += dur
    return len(maxHeap)

print(scheduleCourse(courses))