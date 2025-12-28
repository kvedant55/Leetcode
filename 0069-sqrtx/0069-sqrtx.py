class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        ans = 0
        while(start <= end):
            mid = (start + end)//2
            if(mid*mid == x):
                ans = mid
                break
            elif mid*mid > x:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans
        