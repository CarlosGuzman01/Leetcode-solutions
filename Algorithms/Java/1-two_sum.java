//version 1

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int firstIndex = 0;
        int secondIndex = 1;
        
        int[] array = new int[2];
        
        while(true){
        int firstNum = nums[firstIndex];
        int secondNum = nums[secondIndex];
        if(firstNum + secondNum == target){
            array[0] = firstIndex;
            array[1] = secondIndex;

            return array;

        }
        if(nums.length - 1 == secondIndex ){

            firstIndex++;
            secondIndex = firstIndex + 1;
        }
        else{
            secondIndex++;
        }

       }

    }
}