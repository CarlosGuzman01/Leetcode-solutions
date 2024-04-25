class Solution {
    public int findClosestNumber(int[] nums) {

        int closest = nums[0];

         for(int i = 1; i < nums.length; i++){
            
            int v = nums[i];
            if(closestCompare(v) < closestCompare(closest)){
                closest = v;
            }else if(closestCompare(v) == closestCompare(closest)){
                closest = Math.max(v, closest);
            }
        
        }


        return closest;
        
    }

     public static int closestCompare(int i){
        return Math.abs(i + 0);
    }


}