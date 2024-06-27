class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        nums.clear()
        for i in s:
            nums.append(i)
        nums.sort()
        b = len(nums)
        return b