
class Solution {
    public int maxFrequencyElements(int[] nums) {
        int counter = 0;
        HashMap<Integer, Integer> map = new HashMap<>();
        int max = 0;

        for(int i : nums){
            map.put(i , map.getOrDefault(i, 0) + 1);
            
            max = Math.max(max, map.get(i)); 
        }

        for(int i: map.keySet()){
            if(map.get(i) == max){
                counter++;
            }
        }

        return max * counter;


    }
}