class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
       int start = 0;
       int end  = nums.size() - 1;
       int mid = start + (end - start) / 2;
       int ansl = -1, ansr = -1;
       vector<int> v;

       while(start <= end){
            if(nums[mid] == target){
                ansl = mid;
                end = mid - 1;
            }
            else if(target > nums[mid]){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
            mid = start + (end - start)/2;
        }
        v.push_back(ansl);

        
        start = 0;
        end = nums.size() - 1;
        mid = start + (end - start)/2;
        while(start <= end){
            if(nums[mid] == target){
                ansr = mid;
                start = mid + 1;
            }
            else if(target > nums[mid]){
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
            mid = start + (end - start) / 2;
        }
        v.push_back(ansr);

        return v;
       
    }
};