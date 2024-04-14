class Solution {
    public boolean isAlienSorted(String[] words, String order) {

        HashMap<Character, Integer> myMap = new HashMap<>();

        boolean flag = true;
 
        
        for(int i = 0; i < order.length(); i++){
            myMap.put(order.charAt(i), i);
        }

        
        for(int i = 0; i < words.length && i + 1 < words.length; i++){ 
            
          if(helperFunction(myMap, i, words, flag) == false) return false; 

        }

        return true;
        
    }

    public static boolean helperFunction(HashMap<Character, Integer> myMap, int i, String[] words, boolean flag){ 

        for(int pointer = 0; pointer < words[i].length() && pointer < words[i + 1].length(); pointer++){

            if(words[i].charAt(pointer) == words[i + 1].charAt(pointer)){
                flag = true;
                continue;
            
            }else if(myMap.get(words[i].charAt(pointer)) < myMap.get(words[i + 1].charAt(pointer))){
                
               return true;
            
            }else if(myMap.get(words[i].charAt(pointer)) > myMap.get(words[i + 1].charAt(pointer))){
                
                return false;
            }

            flag = false;
            
        }

        if(flag && words[i].length() > words[i + 1].length()){

            return false;
            
        }
        
        return true;

    }


}