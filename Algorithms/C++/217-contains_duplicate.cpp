class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        std::unordered_set<int> mySet;

        for(int n : nums){
            auto temp = mySet.find(n);

            if(temp != mySet.end()){
                return true;
            }

            mySet.insert(n);
        }

        return false;

    }
};