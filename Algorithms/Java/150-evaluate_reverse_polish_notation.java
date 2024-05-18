class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int op = 0;
        
        for(String c : tokens){
            if(c.equals("+") || c.equals("-") || c.equals("/") || c.equals("*")){
                int temp1 = stack.pop();
                int temp2 = stack.pop();

                if(c.equals("+")){
                    op = temp2 + temp1;
                
                }else if(c.equals("-")){
                    op = temp2 - temp1;
                
                }else if(c.equals("*")){
                    op = temp2 * temp1;
               
                }else if(c.equals("/")){
                    op = temp2 / temp1;
                }

                stack.push(op);
                


            }else{
                stack.push(Integer.parseInt(c));
            }   
        }

        return stack.pop();
        
    }
}