class Solution {
    public int sumOfUnique(int[] nums) {

        int total = 0;
        HashMap<Integer, Integer> myMap = new HashMap<>();

        for(int i : nums){
            myMap.put(i, myMap.getOrDefault(i, 0) + 1);
        }

        for(int i: myMap.keySet()){
            if(myMap.get(i) == 1){
                total = total + i;
            }
        }


        return total;
        
    }
}