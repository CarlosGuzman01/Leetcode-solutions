class Solution {
    public int countCharacters(String[] words, String chars) {

        HashMap<Character, Integer> original = new HashMap<>();
        HashMap<Character, Integer> copy = new HashMap<>();
        int totalChars = 0;
        boolean flag = true;

        for(char c: chars.toCharArray()){
            original.put(c, original.getOrDefault(c, 0) + 1);
        }

        for(int i = 0; i < words.length; i++){
            copy.putAll(original);
            flag = true;

            for(int j = 0; j < words[i].length(); j++ ){

                if(copy.containsKey(words[i].charAt(j)) && copy.get(words[i].charAt(j)) > 0 ){
                    copy.put(words[i].charAt(j), copy.get(words[i].charAt(j)) - 1);
                
                }else{
                    flag = false;
                    break;
                }

            }

            if(flag){
                totalChars =  totalChars + words[i].length();
            }


        }

        return totalChars;
     }

}