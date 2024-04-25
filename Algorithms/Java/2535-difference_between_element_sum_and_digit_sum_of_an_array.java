class Solution {
    public int differenceOfSum(int[] nums) {
        int totalNumber = 0;
        int totalDigit  = 0;

        for(int i : nums){
            totalNumber = totalNumber + i;
            while(i != 0){
               totalDigit = totalDigit + i % 10;
               i =  i / 10; 
            }
        }


        return Math.abs(totalDigit -  totalNumber);
        
    }
}