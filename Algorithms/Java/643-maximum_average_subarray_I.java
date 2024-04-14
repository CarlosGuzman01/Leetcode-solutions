class Solution {
    public double findMaxAverage(int[] nums, int k) {

        int low = 0;
        double answer = Integer.MIN_VALUE;
        double current = 0;

        for(int high = 0; high < nums.length; high++){
            
            current += nums[high];
            
            if(high >= k - 1){
                answer = Math.max(answer, current);
                current -= nums[low];
                low++;
            }
        }

        return answer/k;

                                                                                                           
    }
}