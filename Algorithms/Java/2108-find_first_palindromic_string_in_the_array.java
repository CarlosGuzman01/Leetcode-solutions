class Solution {
    public String firstPalindrome(String[] words) {

        String answer = "";

        for(String s : words){
            if(s.equals(reverseString(s))) return answer = s;
        }

        return answer;

        
    }

     public static String reverseString(String s){

        StringBuilder sb = new StringBuilder(s);
        
        int low = 0;
        int high = s.length() - 1;

        while(low < high){
            char temp = s.charAt(low);
            sb.setCharAt(low, s.charAt(high));
            sb.setCharAt(high, temp);


            low++;
            high--;
        }

        return sb.toString();
    }


}