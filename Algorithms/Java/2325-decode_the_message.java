class Solution {
    public String decodeMessage(String key, String message) {

        HashSet<Character> keySet = new HashSet<>();
        String letters = "abcdefghijklmnopqrstuvwxyz";
        HashMap<Character, Character> myMap = new HashMap<>();
        StringBuilder builder = new StringBuilder();
        ArrayList<Character> myList = new ArrayList<>();


        for(int i = 0;  i < key.length(); i++){
            while(key.charAt(i) == ' '){
                i++;
            }

            if(!keySet.contains(key.charAt(i))){
                keySet.add(key.charAt(i));
                myList.add(key.charAt(i));
            }
        }

       for(int i = 0; i < letters.length(); i++){
        myMap.put(myList.get(i), letters.charAt(i));
       
       }

       for(int i = 0; i < message.length(); i++){
           if(message.charAt(i) == ' '){
            builder.append(' ');
            
            }else{
                builder.append(myMap.get(message.charAt(i)));

            }
       }

        return builder.toString();
    
        
    }
}