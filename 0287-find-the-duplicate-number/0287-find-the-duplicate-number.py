class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i in d:
                return i
            else:
                d.add(i)    