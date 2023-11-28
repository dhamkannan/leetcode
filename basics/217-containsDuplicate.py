
nums = [1,2,3,1]
n = 9 

def containsDuplicate():
    duplicateSet = set()
    for n in nums:
        if n in duplicateSet:
            return True
        else:
            duplicateSet.add(n)
    return False


containsDuplicate()