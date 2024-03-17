class Solution {
    public int firstUniqChar(String s) {

        HashMap<Character, Integer> myMap = new HashMap<>();

        for(int i = 0; i < s.length(); i++){

            myMap.put(s.charAt(i), myMap.getOrDefault(s.charAt(i), 0) + 1);

        }

        if(!myMap.containsValue(1)){
            return -1;
        }

        for(int i = 0; i < s.length(); i++){
            if(myMap.get(s.charAt(i)) == 1){
                return i;

            }
        }


        return 999; //mandatory return statement

   
    }
}