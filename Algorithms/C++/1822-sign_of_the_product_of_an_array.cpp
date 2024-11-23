class Solution {
public:
    int arraySign(vector<int>& nums) {
        
        bool b;

        if(nums[0] > 0 ){
            b = true;

        }else if(nums[0] < 0){
            b = false;

        }else{
            return 0;
        }

        for(int i = 1; i < nums.size(); i++){
            if(nums[i] == 0){
                return 0;
            
            }else if(nums[i] < 0){
                b = !b;
            }
        }

        if(b) return 1;
        return -1;
    }
};