class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int ans = 0;

        unordered_set<int> set;

        for(int i = nums.size() - 1; i >= 0; i--){

            if(nums[i] <= k){
                set.insert(nums[i]);
            }

            ans++;

            if(set.size() == k){
                return ans;
            }

        }

        return ans;

    }
};