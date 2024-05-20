class Solution {
    public String sortSentence(String s) {
        String[] arr = s.split(" ");
       String[] arr2 = new String[arr.length];

       StringBuilder sb = new StringBuilder();

       for(String str: arr){
            arr2[helper(str)] = str; 
       }

       for(String p: arr2){ 
        sb.append(p);
        sb.deleteCharAt(sb.length() - 1);
        sb.append(" ");
       }

        sb.deleteCharAt(sb.length() - 1);

       return sb.toString();
        
    }

      public static int helper(String s){
        StringBuilder sb =  new StringBuilder(s);
        int index = Character.getNumericValue(sb.charAt(sb.length() - 1));
        
        return index - 1;
    }


}