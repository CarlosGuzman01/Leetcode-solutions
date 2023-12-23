class Solution {
    public int majorityElement(int[] nums) {

        int candidate = 0;
        int counter = 0;

        for(int n: nums){

            if(counter == 0){
                candidate = n;
            }

            if(candidate == n){
                counter++;
            
            }else{
                counter--;
            }

        }
        return candidate;

    }
}