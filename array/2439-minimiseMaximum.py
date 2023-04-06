"""
Time: o(n)
Memory: o(1)
"""

import math
# nums = [3,7,1,6]
# nums = [13,13,20,0,8,9,9]
nums = [439,228,482,150,231,209,991,125,453,407,670,491,300,125,285,749,350,411,527,768]
def minimizeArrayValue(nums):
    res = nums[0]
    total = nums[0]
    for i in range(1,len(nums)):
        total += nums[i]
        avg = math.ceil(total / (i+1))
        res = max(res, avg)
    return res
print(minimizeArrayValue(nums))
