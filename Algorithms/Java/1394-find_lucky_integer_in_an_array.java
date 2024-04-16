class Solution {
    public int findLucky(int[] arr) {

        HashMap<Integer,Integer> myMap = new HashMap<>();
        int result = -1;
        

        for(int i : arr){
            myMap.put(i, myMap.getOrDefault(i, 0)  + 1);
        }

        for(int i: arr){
            if(i == myMap.get(i)){
                if(result < i){
                    result = i;
                }
            }
        }

        return result;
        
    }
}