class Solution {
public:
    double myPow(double x, int n) {
        double power = 1;
        if(n < 0){
            x = 1/x;

        long num = labs(n);

        }
        while(long num != 0){
            if((num & 1) != 0){
                power = power * x;
                x = x*x;
                num = num / 2;
            }
        }
        return power;
    }
};