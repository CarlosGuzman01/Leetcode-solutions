class Solution {
    public int calPoints(String[] operations) {

        Stack<Integer> myStack = new Stack<>();
        int total = 0;

        for(String s: operations){
            if (s.equals("C")) {
                myStack.pop(); 
            
            }else if(s.equals("D")){
                myStack.push(myStack.peek() * 2);     
            
            }else if (s.equals("+")){
                int temp1 = myStack.pop();
                int temp2 = myStack.pop();

                int value =  temp1 + temp2;

                myStack.push(temp2);
                myStack.push(temp1);
                myStack.push(value);
            
            }else{
                myStack.push(Integer.parseInt(s));
            }
        }

        while(!myStack.isEmpty()){
            total += myStack.pop();
        }


        return total;
        
    }
}