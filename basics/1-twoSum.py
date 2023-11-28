class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in tempMap:
                return [tempMap[diff], i]
            tempMap[n] = i