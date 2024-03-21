class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {


        HashSet<Integer> mySet = new HashSet<>();

        int left = 0;
        for(int right = 0; right < nums.length; right++){

            if(right - left > k){

                mySet.remove(nums[left]);
                left++;

            }

            if(mySet.contains(nums[right])){
                return true;

            }

            mySet.add(nums[right]);

        }
        return false;
        
    }
}