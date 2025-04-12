class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> minutes;
        for(int i = 0; i < timePoints.size(); i++){
            string current = timePoints[i];
    
        int hours = stoi(current.substr(0,2));
        int min = stoi(current.substr(3,2));
        int total = hours * 60 + min;
        minutes.push_back(total); 
        }

        // Step-2: Sort
        sort(minutes.begin(), minutes.end());

        // Step-3: Calculate min differende
        int mini = INT_MAX;
        int n = minutes.size();

        for(int i = 0 ; i < n-1; i++){
            int diff = minutes[i+1] - minutes[i];
            mini = min(mini, diff);
        }

        int lastdiff  = (minutes[0] + 1440) - minutes[n - 1];
        mini = min(mini, lastdiff);

        return mini;
    }
};