class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        
        HashMap<Character, Integer> myMap1 = new HashMap<>();
        HashMap<Character, Integer> myMap2= new HashMap<>();
        Map<Integer, Character> myMap = new HashMap<>();
        
        int swapsCounter = 0;

        if(s1.equals(s2)) return true;

        int i = 0;
        for(char c : s1.toCharArray()){
            myMap.put(i, c);
            myMap1.put(c, myMap1.getOrDefault(c, 0) + 1);
            i++;
        }


        for(char c : s2.toCharArray()){
            myMap2.put(c, myMap2.getOrDefault(c, 0) + 1);
        }

        for(int j = 0; j < s1.length(); j++){
            
            if(myMap.get(j) != s2.charAt(j)){
                swapsCounter++;
                if(swapsCounter > 2) return false;
            }

         
            char temp = s1.charAt(j);

            if(myMap1.get(temp) != myMap2.get(temp)) return false;

                
        }
        

        return true;
        
    }
}