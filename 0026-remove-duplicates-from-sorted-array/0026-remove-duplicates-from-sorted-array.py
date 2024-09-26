class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        
        # Add unique elements to the new list
        for i in range(nums[0], nums[-1] + 1):
            if i in nums:
                l.append(i)
        
        # Modify nums in place
        nums[:len(l)] = l  # Replace the first part of nums with the unique elements
        
        return len(l)  # Return the number of unique elements
