//version 2

import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        int complement;
        int[] solution = new int[2];

        HashMap<Integer, Integer> myMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){

            complement = target - nums[i];

            if(myMap.containsKey(complement)){

                solution[0] = myMap.get(complement);
                solution[1] = i;

                return solution;
                
            }

            myMap.put(nums[i], i);

        }    

       return null;
    }

}