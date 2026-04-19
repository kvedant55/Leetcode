class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = (n * (n + 1))//2
        array_sum = sum(nums)
        return sum1 - array_sum
        