class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        if(nums.size() == 1) return true;

        bool in = true;
        
        if(nums[0] > nums[nums.size() - 1]) in = false;

        for(int i = 0; i < nums.size() && i + 1 < nums.size(); i++){
            if(in){
                if(nums[i] > nums[i + 1]){
                    return false;
                }
            }else{
                 if(nums[i] < nums[i + 1]){
                    return false;
                }

            }
    
        }

        return true;
    }
};