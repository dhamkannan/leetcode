class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if i > 0  and nums[i-1] == n:
                continue
            l, r = i+1, len(nums)-1

            while l < r:
                threeSum = n + nums[l] + nums[r]

                if threeSum > 0:
                    r = r-1
                elif threeSum < 0:
                    l = l+1
                else:
                    res.append([n, nums[l], nums[r]])
                    l = l+1
                    r = r-1
                    while l < r and nums[l] == nums[l-1]:
                        l = l +1
        return res
        