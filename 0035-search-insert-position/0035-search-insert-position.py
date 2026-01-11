class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        pos = -1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                pos = mid
                return pos
            elif target > nums[mid]:
                start = mid + 1
                if target == nums[mid] + 1:
                    return mid + 1
            else:
                end = mid - 1
                if target == nums[mid] - 1 and mid == 0:
                    return mid 
        return pos