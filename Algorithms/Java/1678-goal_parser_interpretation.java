class Solution {
    public String interpret(String command) {

        StringBuilder answer = new StringBuilder();

        for(int i = 0; i < command.length() && i + 1 < command.length(); i++){

            if(command.charAt(i) == 'G'){
                answer.append('G');
            }else if(command.charAt(i) == '(' && command.charAt(i + 1) == ')'){
                answer.append('o');
            }else if(command.charAt(i) == '(' && command.charAt(i + 1) == 'a'){
                answer.append("al");
            }


        }

        if (command.charAt(command.length() - 1) == 'G') {

            answer.append('G');
            
        }

        return answer.toString();
        
    }
}