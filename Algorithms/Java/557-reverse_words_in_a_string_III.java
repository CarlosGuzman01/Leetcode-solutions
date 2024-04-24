class Solution {
    public String reverseWords(String s) {

        StringBuilder sb = new StringBuilder();

        String[] array = s.split("\s+");

        for(String f: array){
            sb.append(reverseOneWrod(f) + " ");
        }

        sb.deleteCharAt(sb.length() - 1);

        return sb.toString();
        

    }
     public static String reverseOneWrod(String s){

        StringBuilder sb =  new StringBuilder(s);


        int low = 0;
        int high = s.length() - 1;

        while(low < high){
            
            char temp = sb.charAt(low);
            sb.setCharAt(low, sb.charAt(high));
            sb.setCharAt(high, temp);

            low++;
            high--;
        }

        return sb.toString();

    }


}