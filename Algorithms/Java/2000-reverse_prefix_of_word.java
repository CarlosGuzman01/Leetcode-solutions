class Solution {
    public String reversePrefix(String word, char ch) {
        StringBuilder sb = new StringBuilder(word);
        int low = 0;
        int high = -1; 

        for(int i = 0; i < word.length(); i++){
            if(word.charAt(i) == ch){
                high = i;
                break;             
            }

        }

        if(high < 0) return word;

        while(low < high){

            char temp = word.charAt(low);
            sb.setCharAt(low, word.charAt(high));
            sb.setCharAt(high, temp);

            low++;
            high--;
        }
         
        return sb.toString(); 
        
    }
}