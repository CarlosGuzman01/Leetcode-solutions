class Solution {
    public int missingNumber(int[] nums) {

       int val1 = 0;
       int val2 = 0;
       int n = nums.length;

       for(int i = 0; i <= n; i++){
        val1 = val1 + i;
       }

       for(int i: nums){
        val2 = val2 + i;
       }


       return val1 - val2;
        
    }
}