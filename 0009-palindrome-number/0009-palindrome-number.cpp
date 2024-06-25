class Solution {
public:
    bool isPalindrome(long x) {
        long rem = 0, ans = 0, num = x;
        if(x < 0 ){
            return false;
        }
        else{
            while(x > 0){
                rem = x % 10;
                ans = ans*10 + rem;
                x = x / 10;
            }

            if(num == ans){
                return true;
            }
            else{
                return false;
            }
        }
    };

};