class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        
        if(nums.size() == 1){
            return true;
        }

        for(int i = 0; i + 1 < nums.size(); i++){
            
            if(even(nums[i]) == even(nums[i + 1])){
                return false;
            }
        }

        return true;
    }

    bool even(int n){
        return n % 2 == 0;
    }
};