
nums = [1,2,3,1]
k = 3 

def containsDuplicate():
    duplicateMap = {}
    for i, n in enumerate(nums):
        if n in duplicateMap:
            if i - duplicateMap[n] <= k:
                return True
            else:
                duplicateMap[n] = i
        else:
            duplicateMap[n] = i
    return False



containsDuplicate()