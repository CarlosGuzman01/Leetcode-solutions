class Solution {
    public int countSeniors(String[] details) {

        int counter = 0;
        String answer = "";
        
        for(String s : details){
            answer = Character.toString(s.charAt(11)) + Character.toString(s.charAt(12));
            if(Integer.parseInt(answer) > 60) counter++;
        }

        return counter;
        
    }
}