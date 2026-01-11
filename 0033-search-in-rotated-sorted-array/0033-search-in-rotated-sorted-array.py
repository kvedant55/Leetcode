class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # In a sorted array, always atleast one side from mid is sorted.
        low = 0
        high = len(nums) - 1
        while(low <= high):
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # If the mid is greater than low, left side is sorted
            elif nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # if the mid is less than high, right side is sorted 
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
