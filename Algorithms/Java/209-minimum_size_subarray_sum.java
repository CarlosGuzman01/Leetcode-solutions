class Solution {
    public int minSubArrayLen(int target, int[] nums) {

        
        int low = 0;
        int current = 0;
        int minSize = Integer.MAX_VALUE;

        for(int high = 0; high < nums.length; high++){
            
            current = current + nums[high];                              

            while(current >= target){
                minSize = Math.min(minSize, (high - low) + 1);

                current = current - nums[low];

                low++;
            }
        }

        if(minSize == Integer.MAX_VALUE){
            return 0;
        }

        return minSize;
        
    }
}