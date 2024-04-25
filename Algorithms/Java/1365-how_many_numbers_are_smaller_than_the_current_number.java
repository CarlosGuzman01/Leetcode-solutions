class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {

        HashMap<Integer, Integer> myMap = new HashMap<>();
        int[] array2 = Arrays.copyOf(nums, nums.length);
        
        Arrays.sort(array2);

        int j = 0;
        for(int i: array2){
            if(!myMap.containsKey(i)){
                myMap.put(i, j);
            }

            j++;   
        }

        for(int i = 0; i < nums.length; i++){
            nums[i] = myMap.get(nums[i]);
        }


        return nums;
        
    }
}