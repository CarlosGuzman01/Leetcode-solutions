class Solution {
    public boolean areOccurrencesEqual(String s) {
        HashMap<Character, Integer> myMap = new HashMap<>();
        HashSet<Integer> mySet = new HashSet<>();

        for(char c: s.toCharArray()){
            myMap.put(c, myMap.getOrDefault(c, 0) + 1);
        }

        for(char c: myMap.keySet()){
            mySet.add(myMap.get(c));

            if(mySet.size() > 1){
                return false;
            }

            
        }



        return true;
        
    }
}