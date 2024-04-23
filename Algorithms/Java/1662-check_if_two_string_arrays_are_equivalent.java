class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {

        if(solution(word1).equals(solution(word2))) return true;
        
        return false;
        
    }

     public static String solution(String[] word){
        StringBuilder sb = new StringBuilder();

        for(String s: word ){
            sb.append(s);
        }

        return sb.toString();
    }


}