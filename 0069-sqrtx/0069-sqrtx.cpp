class Solution {
public:
    int mySqrt(int x) {
        int start = 0;
        int end = x,mid,ans = 0;
        while(start <= end){
            mid = start + (end - start)/2;
            if(((long)mid*mid) > (long)x){
                end = mid - 1;
            }
            else if(((long)mid*mid) < (long)x){
                ans = mid;
                start = mid + 1;
            }
            if(((long)mid*mid) == x){
                ans = mid;
                break;
            }
        }
        return ans;
    }
};