class Solution {
    public boolean uniqueOccurrences(int[] arr) {

        HashMap<Integer, Integer> myMap = new HashMap<>();
        HashSet<Integer> mySet = new HashSet<>();

        for(int i: arr){
            myMap.put(i, myMap.getOrDefault(i, 0) + 1);
        }

      for(int i: myMap.keySet()){
        if (mySet.contains(myMap.get(i))) {
            return false;
            
        }

        mySet.add(myMap.get(i));
      }

        return true;
        
    }
}