class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
        int total = 0;
        int total2 = 0;

        for(int n: nums){
            total += n;
        }
        
        int n = nums.size();
        total2 = n * (n + 1)/2;

        return total2 - total;
        
    }
};