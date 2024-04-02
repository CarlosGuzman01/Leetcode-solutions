class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        HashMap<Character, Character> sMap = new HashMap<>();
        HashMap<Character, Character> tMap = new HashMap<>();

        for(int i = 0; i < s.length(); i++){

            if((sMap.containsKey(s.charAt(i)) && sMap.get(s.charAt(i)) != t.charAt(i))  || tMap.containsKey(t.charAt(i)) && tMap.get(t.charAt(i)) != s.charAt(i) ){
                return false;
            }
            
            sMap.put(s.charAt(i), t.charAt(i));
            tMap.put(t.charAt(i), s.charAt(i));

        }

        return true;

    }
}