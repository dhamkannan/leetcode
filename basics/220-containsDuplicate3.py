
nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0

def containsDuplicate():
    for i in range(len(nums)):
        for j in range(i+1, min((i + indexDiff+1), len(nums))):
            if abs(nums[i] - nums[j]) <= valueDiff:
                return True
    return False



containsDuplicate()