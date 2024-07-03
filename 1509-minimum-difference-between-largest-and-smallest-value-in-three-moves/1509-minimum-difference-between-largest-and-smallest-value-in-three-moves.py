from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        minVal = float('inf')
        n = len(nums)
        if(n <= 4):
            return 0
        
        minVal = min(minVal, nums[n - 4] - nums[0])
        minVal = min(minVal, nums[n - 1] - nums[3])
        minVal = min(minVal, nums[n - 2] - nums[2])
        minVal = min(minVal, nums[n - 3] - nums[1])

        return minVal
        